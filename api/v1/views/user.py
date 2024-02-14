#!/usr/bin/python3
"""
This module defines the User view.
"""

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from models import storage
from models.user import User
from api.v1.views import app_views  # Import app_views

# Function to hash a password
def hash_password(password):
    return generate_password_hash(password)

# Function to check a password against its hash
def check_password(hashed_password, password):
    return check_password_hash(hashed_password, password)

# API endpoint for listing all users
@app_views.route('/users', methods=['GET'])  # Use app_views as a decorator
def list_users():
    users = storage.all(User).values()
    user_list = [user.to_dict() for user in users]
    return jsonify(user_list)

# API endpoint for retrieving a specific user
@app_views.route('/users/<user_id>', methods=['GET'])  # Use app_views as a decorator
def get_user(user_id):
    user = storage.get(User, user_id)
    if user:
        return jsonify(user.to_dict())
    else:
        return jsonify({'error': 'User not found'}), 404

# API endpoint for deleting a user
@app_views.route('/users/<user_id>', methods=['DELETE'])  # Use app_views as a decorator
def delete_user(user_id):
    user = storage.get(User, user_id)
    if user:
        storage.delete(user)
        storage.save()
        return jsonify({}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

# Example endpoint for creating a new user
@app_views.route('/api/v1/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Missing username or password'}), 400

    # Hash the password before creating a new user
    data['password'] = hash_password(data['password'])
    
    new_user = User(**data)
    storage.new(new_user)
    storage.save()

    return jsonify(new_user.to_dict()), 201

# API endpoint for updating a user
@app_views.route('/users/<user_id>', methods=['PUT'])  # Use app_views as a decorator
def update_user(user_id):
    user = storage.get(User, user_id)
    if user:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Not a JSON'}), 400

        for key, value in data.items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(user, key, value)

        storage.save()
        return jsonify(user.to_dict()), 200
    else:
        return jsonify({'error': 'User not found'}), 404
