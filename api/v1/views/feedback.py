#!/usr/bin/python3
"""
This module defines the Feedback view.
"""

from flask import Flask, jsonify, request
from api.v1.views import app_views
from models import storage
from models.feedback import Feedback

@app_views.route('/feedbacks', methods=['GET'])
def list_feedbacks():
    feedbacks = storage.all(Feedback).values()
    feedback_list = [f.to_dict() for f in feedbacks]
    return jsonify(feedback_list)

@app_views.route('/feedbacks/<feedback_id>', methods=['GET'])
def get_feedback(feedback_id):
    feedback = storage.get(Feedback, feedback_id)
    if feedback:
        return jsonify(feedback.to_dict())
    else:
        return jsonify({'error': 'Feedback not found'}), 404

@app_views.route('/feedbacks/<feedback_id>', methods=['DELETE'])
def delete_feedback(feedback_id):
    feedback = storage.get(Feedback, feedback_id)
    if feedback:
        storage.delete(feedback)
        storage.save()
        return jsonify({}), 200
    else:
        return jsonify({'error': 'Feedback not found'}), 404

@app_views.route('/feedbacks', methods=['POST'])
def create_feedback():
    data = request.get_json()
    if not data or 'user_id' not in data or 'technician_id' not in data \
            or 'rating' not in data or 'comments' not in data \
            or 'timestamp' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    new_feedback = Feedback(**data)
    storage.new(new_feedback)
    storage.save()

    return jsonify(new_feedback.to_dict()), 201

@app_views.route('/feedbacks/<feedback_id>', methods=['PUT'])
def update_feedback(feedback_id):
    feedback = storage.get(Feedback, feedback_id)
    if feedback:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Not a JSON'}), 400

        for key, value in data.items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(feedback, key, value)

        storage.save()
        return jsonify(feedback.to_dict()), 200
    else:
        return jsonify({'error': 'Feedback not found'}), 404
