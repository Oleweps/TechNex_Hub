#!/usr/bin/python3
"""
This module defines the Suggestion view.
"""

from flask import Flask, jsonify, request
from api.v1.views import app_views
from models import storage
from models.suggestion import Suggestion
from models.user import User  # Add this import

@app_views.route('/suggestions', methods=['GET'])
def list_suggestions():
    suggestions = storage.all(Suggestion).values()
    suggestion_list = [s.to_dict() for s in suggestions]
    return jsonify(suggestion_list)

# Example endpoint for retrieving suggestions for a user
@app_views.route('/users/<user_id>/suggestions', methods=['GET'])
def get_user_suggestions(user_id):
    user = storage.get(User, user_id)

    if user:
        # Accessing the 'suggestions' relationship to get all user's suggestions
        suggestions = user.suggestions
        suggestion_list = [suggestion.to_dict() for suggestion in suggestions]
        return jsonify(suggestion_list)
    else:
        return jsonify({'error': 'User not found'}), 404

@app_views.route('/suggestions/<suggestion_id>', methods=['GET'])
def get_suggestion(suggestion_id):
    suggestion = storage.get(Suggestion, suggestion_id)
    if suggestion:
        return jsonify(suggestion.to_dict())
    else:
        return jsonify({'error': 'Suggestion not found'}), 404

@app_views.route('/suggestions/<suggestion_id>', methods=['DELETE'])
def delete_suggestion(suggestion_id):
    suggestion = storage.get(Suggestion, suggestion_id)
    if suggestion:
        storage.delete(suggestion)
        storage.save()
        return jsonify({}), 200
    else:
        return jsonify({'error': 'Suggestion not found'}), 404

@app_views.route('/suggestions', methods=['POST'])
def create_suggestion():
    data = request.get_json()
    if not data or 'user_id' not in data or 'content' not in data or 'timestamp' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    new_suggestion = Suggestion(**data)
    storage.new(new_suggestion)
    storage.save()

    return jsonify(new_suggestion.to_dict()), 201

@app_views.route('/suggestions/<suggestion_id>', methods=['PUT'])
def update_suggestion(suggestion_id):
    suggestion = storage.get(Suggestion, suggestion_id)
    if suggestion:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Not a JSON'}), 400

        for key, value in data.items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(suggestion, key, value)

        storage.save()
        return jsonify(suggestion.to_dict()), 200
    else:
        return jsonify({'error': 'Suggestion not found'}), 404
