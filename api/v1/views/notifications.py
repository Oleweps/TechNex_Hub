#!/usr/bin/python3
"""
This module defines the Notification view.
"""

from flask import Flask, jsonify, request
from api.v1.views import app_views
from models import storage
from models.notification import Notification

@app_views.route('/notifications', methods=['GET'])
def list_notifications():
    notifications = storage.all(Notification).values()
    notification_list = [n.to_dict() for n in notifications]
    return jsonify(notification_list)

@app_views.route('/notifications/<notification_id>', methods=['GET'])
def get_notification(notification_id):
    notification = storage.get(Notification, notification_id)
    if notification:
        return jsonify(notification.to_dict())
    else:
        return jsonify({'error': 'Notification not found'}), 404

@app_views.route('/notifications/<notification_id>', methods=['DELETE'])
def delete_notification(notification_id):
    notification = storage.get(Notification, notification_id)
    if notification:
        storage.delete(notification)
        storage.save()
        return jsonify({}), 200
    else:
        return jsonify({'error': 'Notification not found'}), 404

@app_views.route('/notifications', methods=['POST'])
def create_notification():
    data = request.get_json()
    if not data or 'user_id' not in data or 'content' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    new_notification = Notification(**data)
    storage.new(new_notification)
    storage.save()

    return jsonify(new_notification.to_dict()), 201

@app_views.route('/notifications/<notification_id>', methods=['PUT'])
def update_notification(notification_id):
    notification = storage.get(Notification, notification_id)
    if notification:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Not a JSON'}), 400

        for key, value in data.items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(notification, key, value)

        storage.save()
        return jsonify(notification.to_dict())
