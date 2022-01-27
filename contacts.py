from flask import Flask, request, jsonify

landline = Flask(__name__)

contacts = [
    {
        "Contact" : 3854990835,
        "Name" : "John Doe",
        "Done" : False,
        "ID" : 1
    },

    {
        "Contact" : 3855110482,
        "Name" : "Jane Doe",
        "Done" : False,
        "ID" : 2
    }
]

@landline.route("/add-contacts", methods = ["POST"])

def add_contacts():
    if not request.json:
       return jsonify({
           "status" : "Error",
           "message" : "Please provide data"

       }, 400) 
    
    contact = {
        "Contact" : request.json["Contact"],
        "Name" : request.json["Name"],
        "Done" : False,
        "ID" : contacts[-1]["ID"]+1
    }

    contacts.append(contact)
    return jsonify({
           "status" : "Success",
           "message" : "Contact added successfully"

       }) 

@landline.route("/get-contacts")
def get_contacts():
    return jsonify({
        "data" : contacts
    })

if(__name__ == "__main__"):
    landline.run(debug = True)