import { useState } from "react";

const ContactForm = ({existingContact = {}, updateCallback}) => {
    const [firstName, setFirstName] = useState(existingContact.firstName || "")
    const [lastName, setLastName] = useState(existingContact.lastName || "")
    const [email, setEmail] = useState(existingContact.email || "")

    //if there is existing data then we are updating
    const updating = Object.entries(existingContact).length !== 0

    const onSubmit = async (e) => {
        e.preventDefault()

        //define data
        const data = {
            firstName,
            lastName,
            email
        }

        //define url endpoint
        const url = "http://127.0.0.1:5000/" + (updating ? `update_contact/${existingContact.id}` : "create_contact")

        //define options for the request
        const options ={
            method: updating ? "PATCH" : "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }

        //setting the request
        const response = await fetch(url, options)

        //checks if the request is successful, alerts with error if not
        if (response.status !== 201 && response.status !== 200) {
            const data = await response.json()
            alert(data.message)
        } else {
            updateCallback()
        }
    }

    return (
        <form onSubmit={onSubmit}>
            <div>
                <label htmlFor="firstName">First Name:</label>
                <input 
                    type="text" 
                    id="firstName" 
                    value={firstName} 
                    onChange={(e) => setFirstName(e.target.value)}
                    />
            </div>
            <div>
                <label htmlFor="lastName">Last Name:</label>
                <input 
                    type="text" 
                    id="lastName" 
                    value={lastName} 
                    onChange={(e) => setLastName(e.target.value)}
                    />
            </div>
            <div>
                <label htmlFor="email">Email:</label>
                <input 
                    type="text" 
                    id="email" 
                    value={email} 
                    onChange={(e) => setEmail(e.target.value)}
                    />
            </div>
            <button type="submit">{updating ? "Update" : "Create Contact"}</button>
        </form>
    );
};

export default ContactForm