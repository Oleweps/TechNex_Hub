#!/usr/bin/python3
"""
This module defines the Message view.
"""

from flask import Flask, jsonify, request
from api.v1.views import app_views
from models import storage
from models.message import Message
from models.user import User  # Add this import

@app_views.route('/messages', methods=['GET'])
def list_messages():
    messages = storage.all(Message).values()
    message_list = [m.to_dict() for m in messages]
    return jsonify(message_list)

@app_views.route('/messages/<message_id>', methods=['GET'])
def get_message(message_id):
    message = storage.get(Message, message_id)
    if message:
        return jsonify(message.to_dict())
    else:
        return jsonify({'error': 'Message not found'}), 404

# Example endpoint for retrieving messages for a user
@app_views.route('/users/<user_id>/messages', methods=['GET'])
def get_user_messages(user_id):
    user = storage.get(User, user_id)

    if user:
        # Accessing the 'received_messages' relationship to get all received messages
        messages = user.received_messages
        message_list = [message.to_dict() for message in messages]
        return jsonify(message_list)
    else:
        return jsonify({'error': 'User not found'}), 404

@app_views.route('/messages/<message_id>', methods=['DELETE'])
def delete_message(message_id):
    message = storage.get(Message, message_id)
    if message:
        storage.delete(message)
        storage.save()
        return jsonify({}), 200
    else:
        return jsonify({'error': 'Message not found'}), 404

@app_views.route('/messages', methods=['POST'])
def create_message():
    data = request.get_json()
    if not data or 'sender_id' not in data or 'receiver_id' not in data \
            or 'timestamp' not in data or 'content' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    new_message = Message(**data)
    storage.new(new_message)
    storage.save()

    return jsonify(new_message.to_dict()), 201

@app_views.route('/messages/<message_id>', methods=['PUT'])
def update_message(message_id):
    message = storage.get(Message, message_id)
    if message:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Not a JSON'}), 400

        for key, value in data.items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(message, key, value)

        storage.save()
        return jsonify(message.to_dict()), 200
    else:
        return jsonify({'error': 'Message not found'}), 404
