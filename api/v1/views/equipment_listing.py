#!/usr/bin/python3
"""
This module defines the EquipmentListing view.
"""

from flask import Flask, jsonify, request, abort  # Import abort
from api.v1.views import app_views
from models import storage
from models.equipment_listing import EquipmentListing
from models.user import User  # Import User

@app_views.route('/equipment_listings', methods=['GET'])
def list_equipment_listings():
    equipment_listings = storage.all(EquipmentListing).values()
    equipment_list = [e.to_dict() for e in equipment_listings]
    return jsonify(equipment_list)

@app_views.route('/equipment_listings/<equipment_id>', methods=['GET'])
def get_equipment_listing(equipment_id):
    equipment_listing = storage.get(EquipmentListing, equipment_id)
    if equipment_listing:
        return jsonify(equipment_listing.to_dict())
    else:
        return jsonify({'error': 'Equipment Listing not found'}), 404

@app_views.route('/equipment_listings/<equipment_id>', methods=['DELETE'])
def delete_equipment_listing(equipment_id):
    equipment_listing = storage.get(EquipmentListing, equipment_id)
    if equipment_listing:
        storage.delete(equipment_listing)
        storage.save()
        return jsonify({}), 200
    else:
        return jsonify({'error': 'Equipment Listing not found'}), 404

@app_views.route('/equipment_listings', methods=['POST'])
def create_equipment_listing():
    data = request.get_json()
    if not data or 'user_id' not in data or 'equipment_name' not in data \
            or 'description' not in data or 'condition' not in data \
            or 'price' not in data or 'contact_details' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    new_equipment_listing = EquipmentListing(**data)
    storage.new(new_equipment_listing)
    storage.save()

    return jsonify(new_equipment_listing.to_dict()), 201

# API endpoint for getting all equipment listings for a specific user
@app_views.route('/users/<user_id>/equipment_listings', methods=['GET'])
def get_user_equipment_listings(user_id):
    user = storage.get(User, user_id)
    if user:
        equipment_listings = user.equipment_listings
        return jsonify([equipment_listing.to_dict() for equipment_listing in equipment_listings])
    else:
        abort(404, 'User not found')

# API endpoint for creating a new equipment listing for a user
@app_views.route('/users/<user_id>/equipment_listings', methods=['POST'])
def create_user_equipment_listing(user_id):
    user = storage.get(User, user_id)
    if user:
        data = request.get_json()
        if not data or 'equipment_name' not in data or 'description' not in data or 'condition' not in data or 'price' not in data or 'contact_details' not in data:
            abort(400, 'Invalid data. Make sure to include all required fields.')
        
        new_equipment_listing = EquipmentListing(user_id=user_id, **data)
        storage.new(new_equipment_listing)
        storage.save()
        
        return jsonify(new_equipment_listing.to_dict()), 201
    else:
        abort(404, 'User not found')

@app_views.route('/equipment_listings/<equipment_id>', methods=['PUT'])
def update_equipment_listing(equipment_id):
    equipment_listing = storage.get(EquipmentListing, equipment_id)
    if equipment_listing:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Not a JSON'}), 400

        for key, value in data.items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(equipment_listing, key, value)

        storage.save()
        return jsonify(equipment_listing.to_dict()), 200
    else:
        return jsonify({'error': 'Equipment Listing not found'}), 404
