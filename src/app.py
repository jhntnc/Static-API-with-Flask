import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)

jackson_family = FamilyStructure("Jackson")

@app.route("/members")
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members)


@app.route("/member/<int:member_id>")
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member)
    else:
        return "Member not found", 404

@app.route("/member", methods=["POST"])
def add_member():
    new_member = request.json
    jackson_family.add_member(new_member)
    return {"message": "Member added successfully", "member": new_member}, 200

@app.route("/member/<int:member_id>", methods=["PUT"])
def update_member(member_id):
    updated_member = request.json
    if jackson_family.update_member(member_id, updated_member):
        return {"message": "Member updated successfully", "member": updated_member}, 200
    else:
        return "Member not found", 404

@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    result = jackson_family.delete_member(id)
    if result['done']:
        return {'done': True}, 200
    else:
        return {'error': 'Member not found'}, 404

if __name__ == "__main__":
    app.run()