#!/usr/bin/python3
"""
This module defines the Admin view.
"""

from flask import Flask, jsonify, request
from api.v1.views import app_views
from models import storage
from models.admin import Admin

@app_views.route('/admins', methods=['GET'])
def list_admins():
    admins = storage.all(Admin).values()
    admin_list = [a.to_dict() for a in admins]
    return jsonify(admin_list)

@app_views.route('/admins/<admin_id>', methods=['GET'])
def get_admin(admin_id):
    admin = storage.get(Admin, admin_id)
    if admin:
        return jsonify(admin.to_dict())
    else:
        return jsonify({'error': 'Admin not found'}), 404

@app_views.route('/admins/<admin_id>', methods=['DELETE'])
def delete_admin(admin_id):
    admin = storage.get(Admin, admin_id)
    if admin:
        storage.delete(admin)
        storage.save()
        return jsonify({}), 200
    else:
        return jsonify({'error': 'Admin not found'}), 404

@app_views.route('/admins', methods=['POST'])
def create_admin():
    data = request.get_json()
    if not data or 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    new_admin = Admin(**data)
    storage.new(new_admin)
    storage.save()

    return jsonify(new_admin.to_dict()), 201

@app_views.route('/admins/<admin_id>', methods=['PUT'])
def update_admin(admin_id):
    admin = storage.get(Admin, admin_id)
    if admin:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Not a JSON'}), 400

        for key, value in data.items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(admin, key, value)

        storage.save()
        return jsonify(admin.to_dict()), 200
    else:
        return jsonify({'error': 'Admin not found'}), 404
