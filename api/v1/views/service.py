#!/usr/bin/python3
"""
This module defines the Service view.
"""

from flask import Flask, jsonify, request
from models import storage
from models.service import Service
from api.v1.views import app_views  # Import app_views

# API endpoint for listing all services
@app_views.route('/services', methods=['GET'])  # Use app_views as a decorator
def list_services():
    services = storage.all(Service).values()
    service_list = [s.to_dict() for s in services]
    return jsonify(service_list)

# API endpoint for retrieving a specific service
@app_views.route('/services/<service_id>', methods=['GET'])  # Use app_views as a decorator
def get_service(service_id):
    service = storage.get(Service, service_id)
    if service:
        return jsonify(service.to_dict())
    else:
        return jsonify({'error': 'Service not found'}), 404

# API endpoint for deleting a service
@app_views.route('/services/<service_id>', methods=['DELETE'])  # Use app_views as a decorator
def delete_service(service_id):
    service = storage.get(Service, service_id)
    if service:
        storage.delete(service)
        storage.save()
        return jsonify({}), 200
    else:
        return jsonify({'error': 'Service not found'}), 404

# API endpoint for creating a new service
@app_views.route('/services', methods=['POST'])  # Use app_views as a decorator
def create_service():
    data = request.get_json()
    if not data or 'name' not in data or 'description' not in data or 'cost' not in data:
        return jsonify({'error': 'Missing name, description, or cost'}), 400

    new_service = Service(**data)
    storage.new(new_service)
    storage.save()

    return jsonify(new_service.to_dict()), 201

# API endpoint for updating a service
@app_views.route('/services/<service_id>', methods=['PUT'])  # Use app_views as a decorator
def update_service(service_id):
    service = storage.get(Service, service_id)
    if service:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Not a JSON'}), 400

        for key, value in data.items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(service, key, value)

        storage.save()
        return jsonify(service.to_dict()), 200
    else:
        return jsonify({'error': 'Service not found'}), 404

