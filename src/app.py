"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the Jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_all_members():
    """Retrieve all family members."""
    members = jackson_family.get_all_members()
    
    return jsonify(members), 200

@app.route('/member', methods=['POST'])
def add_new_member():
    """Add a new family member."""
    body = request.json

    # Validate request body
    required_fields = ["first_name", "age", "lucky_numbers"]
    for field in required_fields:
        if body.get(field) is None:
            return jsonify({"error": f"Falta el campo: {field}"}), 400

    new_member = jackson_family.add_member(body)
    return jsonify(new_member), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    """Retrieve a specific family member by ID."""
    member = jackson_family.get_member(member_id)
    if member is None:
        return jsonify({"error": "No se encontró ningún ID"}), 404
    return jsonify(member), 200

@app.route('/member/<int:member_id>', methods=['DELETE'])
def remove_member(member_id):
    """Delete a specific family member by ID."""
    deleted_member = jackson_family.delete_member(member_id)
    if deleted_member is None:
        return jsonify({"error": "No se encontró el ID"}), 404
    return jsonify({"member": deleted_member,"done":True}), 200

# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)