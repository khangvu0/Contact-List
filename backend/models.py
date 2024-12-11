#contains all our database models - how we interact with our database
from config import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)     #String(80) - 80 is the maximum length
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    #can take all the different fields on our object and convert it into python dictionary which we can then convert 
    #into JSON which is something we can pass from our API
    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }