# CRUD = CREATE, READ, UPDATE, DELETE

from flask import request, jsonify
from config import app, db
from models import Contact

@app.route('/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = [contact.to_json() for contact in contacts] # or list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts":json_contacts})

@app.route('/create_contact',methods= ['POST'])
def create_contacts():
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    email = request.json.get('email')
    print(first_name, last_name, email)

    if not first_name or not last_name or not email:
        return (jsonify({"message": "You must include a first name, last name and email"}),400,)

    new_contact = Contact(first_name=first_name, last_name=last_name, email=email) 
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message":"User created!"}),201

@app.route('/update_contacts/<int:user_id>', methods=['PUT']) # PATCH is also fine
def update_contacts(user_id):# user_id match above user_id in the route
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found"}), 404
    
    data = request.json
    contact.first_name = data.get('first_name', contact.first_name) 
    contact.last_name = data.get('last_name', contact.last_name)
    contact.email = data.get('email', contact.email)
    try:
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    return jsonify({"message": "User updated!"}), 200

@app.route('/delete_contacts/<int:user_id>', methods=['DELETE'])
def delete_contacts(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found"}), 404
    
    try:
        db.session.delete(contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "User deleted!"}), 200



if __name__ == '__main__':
    # once the file runs, create the database if not exist
    with app.app_context():
        db.create_all()

    # Run the server
    app.run(debug=True)


