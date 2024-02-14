#!/usr/bin/python3
"""
This module defines the ServiceRequest view.
"""

from flask import Flask, jsonify, request
from models import storage
from models.service_request import ServiceRequest
from api.v1.views import app_views  # Import app_views

# API endpoint for listing all service requests
@app_views.route('/service_requests', methods=['GET'])  # Use app_views as a decorator
def list_service_requests():
    service_requests = storage.all(ServiceRequest).values()
    service_request_list = [sr.to_dict() for sr in service_requests]
    return jsonify(service_request_list)

# API endpoint for retrieving a specific service request
@app_views.route('/service_requests/<service_request_id>', methods=['GET'])  # Use app_views as a decorator
def get_service_request(service_request_id):
    service_request = storage.get(ServiceRequest, service_request_id)
    if service_request:
        return jsonify(service_request.to_dict())
    else:
        return jsonify({'error': 'ServiceRequest not found'}), 404

# API endpoint for deleting a service request
@app_views.route('/service_requests/<service_request_id>', methods=['DELETE'])  # Use app_views as a decorator
def delete_service_request(service_request_id):
    service_request = storage.get(ServiceRequest, service_request_id)
    if service_request:
        storage.delete(service_request)
        storage.save()
        return jsonify({}), 200
    else:
        return jsonify({'error': 'ServiceRequest not found'}), 404

# API endpoint for creating a new service request
@app_views.route('/service_requests', methods=['POST'])  # Use app_views as a decorator
def create_service_request():
    data = request.get_json()
    if not data or 'user_id' not in data or 'service_type' not in data:
        return jsonify({'error': 'Missing user_id or service_type'}), 400

    new_service_request = ServiceRequest(**data)
    storage.new(new_service_request)
    storage.save()

    return jsonify(new_service_request.to_dict()), 201

# API endpoint for updating a service request
@app_views.route('/service_requests/<service_request_id>', methods=['PUT'])  # Use app_views as a decorator
def update_service_request(service_request_id):
    service_request = storage.get(ServiceRequest, service_request_id)
    if service_request:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Not a JSON'}), 400

        for key, value in data.items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(service_request, key, value)

        storage.save()
        return jsonify(service_request.to_dict()), 200
    else:
        return jsonify({'error': 'ServiceRequest not found'}), 404

