from flask import request, jsonify
from config import app, db
from models import Contact


@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()  #gets all the contacts in the database (Python objects)

    #takes all the elements in contacts, and all the contacts have the to_json method so we call 
    #this method for all the contacts and create a new list that just contains the json of the contact
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})

#CREATE Route
@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    #checks if the values above exist, returns error message if does not exist
    if not first_name or not last_name or not email:
        return (
            jsonify({"message": "You must include a first name, last name and email"}),
            400,        #400 means bad request
        )

    #if first name, last name and email values are valid
    #creates a new contact object that has these different fields that were passed in and can now add to database
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    try:
        db.session.add(new_contact)     #add to the database session, once added it is in the staging area
        db.session.commit()             #adds anything in the staging area, writes it into database permanently, but errors can happen
    except Exception as e:              #catch any exceptions/errors and send error code
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "User created!"}), 201   #201 means new resource created on server

#UPDATE Route
@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found"}), 404

    #modifies the first name in contact to be equal to whatever the json data's first name that was given
    data = request.json
    contact.first_name = data.get("firstName", contact.first_name)  #.get - returns first parameter if
    contact.last_name = data.get("lastName", contact.last_name)     #it exists, if not then second.
    contact.email = data.get("email", contact.email)                #In this case it keeps the same value

    db.session.commit() #makes changes permanent

    return jsonify({"message": "Usr updated."}), 200

#DELETE Route
@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)

    #checks if the user does not exist
    if not contact:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "User deleted!"}), 200


if __name__ == "__main__":
    #spin up the database if it doesn't already exist
    with app.app_context():
        db.create_all()

    app.run(debug=True)