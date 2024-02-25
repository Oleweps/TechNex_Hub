#!/usr/bin/python3
"""
Contains the admin equipment details routes
"""
from flask import Flask, render_template, request, redirect, url_for, jsonify
from models.equipment_listing import EquipmentListing
from models import storage
import uuid

app = Flask(__name__)

@app.route('/equipment_details/<int:equipment_id>', methods=['GET'])
def equipment_details(equipment_id):
    # Fetch equipment details from the database based on equipment_id
    equipment = storage.get(EquipmentListing, id=equipment_id)

    # Generate a UUID as the cache_id
    cache_id = str(uuid.uuid4())

    return render_template('equipment_details.html', equipment=equipment, cache_id=cache_id)

@app.route('/contact-seller', methods=['POST'])
def contact_seller():
    if request.method == 'POST':
        equipment_id = request.form.get('equipment_id')

        # Fetch equipment details from the database based on equipment_id
        equipment = storage.get(EquipmentListing, id=equipment_id)

        # You can implement the logic to handle contacting the seller
        # For demonstration purposes, we'll just return a success message with equipment details
        response_data = {
            'message': 'Contacting seller successful',
            'equipment_name': equipment.equipment_name,
            'seller_contact_details': equipment.contact_details,
        }
        return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
