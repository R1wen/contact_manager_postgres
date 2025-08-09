from contact import (
    add_contact,
    create_table,
    delete_contact,
    list_contact,
    update_contact,
    find_contact
)
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = list_contact()
    return jsonify(contacts), 200


@app.route("/contacts/<int:id>", methods=["GET"])
def get_contact(id):
    contact = find_contact(id)
    return jsonify(contact), 200


@app.route("/contacts", methods=["POST"])
def create_contact():
    data = request.json
    add_contact(data["nom"], data["prenom"], data["telephone"])
    return jsonify({"message": "Contact ajouté avec succès"}), 201


@app.route("/contacts/<int:id>", methods=["DELETE"])
def remove_contact(id):
    delete_contact(id)
    return jsonify({"message": "Contact supprimé"}), 200


@app.route("/contacts/<int:id>", methods=["PUT"])
def edit_contact(id):
    data = request.json
    update_contact(id, data["nom"], data["prenom"], data["telephone"])
    return jsonify({"message": "Contact modifier"}), 200


if __name__ == "__main__":
    create_table()
    app.run(debug=True)
