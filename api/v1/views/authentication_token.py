#!/usr/bin/python3
"""
This module defines the AuthenticationToken view.
"""

from flask import Flask, jsonify, request
from api.v1.views import app_views
from models import storage
from models.authentication_token import AuthenticationToken

@app_views.route('/authentication_tokens', methods=['GET'])
def list_authentication_tokens():
    tokens = storage.all(AuthenticationToken).values()
    token_list = [t.to_dict() for t in tokens]
    return jsonify(token_list)

@app_views.route('/authentication_tokens/<token_id>', methods=['GET'])
def get_authentication_token(token_id):
    token = storage.get(AuthenticationToken, token_id)
    if token:
        return jsonify(token.to_dict())
    else:
        return jsonify({'error': 'Authentication token not found'}), 404

@app_views.route('/authentication_tokens/<token_id>', methods=['DELETE'])
def delete_authentication_token(token_id):
    token = storage.get(AuthenticationToken, token_id)
    if token:
        storage.delete(token)
        storage.save()
        return jsonify({}), 200
    else:
        return jsonify({'error': 'Authentication token not found'}), 404

@app_views.route('/authentication_tokens', methods=['POST'])
def create_authentication_token():
    data = request.get_json()
    if not data or 'user_id' not in data or 'token' not in data \
            or 'expiration_time' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    new_token = AuthenticationToken(**data)
    storage.new(new_token)
    storage.save()

    return jsonify(new_token.to_dict()), 201

@app_views.route('/authentication_tokens/<token_id>', methods=['PUT'])
def update_authentication_token(token_id):
    token = storage.get(AuthenticationToken, token_id)
    if token:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Not a JSON'}), 400

        for key, value in data.items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(token, key, value)

        storage.save()
        return jsonify(token.to_dict()), 200
    else:
        return jsonify({'error': 'Authentication token not found'}), 404
