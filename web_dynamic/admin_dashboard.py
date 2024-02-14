#!/usr/bin/python3
"""
Contains the admin dashboard routes
"""
from flask import Flask, render_template, jsonify
from models.storage import Storage
from models.user import User
from models.service_request import ServiceRequest
from models.equipment_listing import EquipmentListing
import uuid

app = Flask(__name__)
storage = Storage()

# Add more routes as needed

@app.route('/admin_dashboard')
def admin_dashboard():
    # Retrieve relevant data from the storage
    users = storage.all(User)  # Adjust based on your data model
    service_requests = storage.all(ServiceRequest)  # Adjust based on your data model
    equipment_listings = storage.all(EquipmentListing)  # Adjust based on your data model

    # Generate a UUID as the cache_id
    cache_id = str(uuid.uuid4())

    # Render the admin dashboard template with dynamic data and cache_id
    return render_template('admin_dashboard.html', users=users, service_requests=service_requests, equipment_listings=equipment_listings, cache_id=cache_id)

# Add more routes as needed

if __name__ == '__main__':
    app.run(debug=True)
