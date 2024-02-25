#!/usr/bin/python3
"""
Contains the admin dashboard routes
"""
from flask import Flask, render_template
from models import storage
from models.user import User  # Import User model, adjust as needed
from models import ServiceRequest, EquipmentListing



app = Flask(__name__)
storage = Storage()

@app.route('/admin_dashboard')
def admin_dashboard():
    # Retrieve relevant data from the storage
    users = storage.all(User)  # Adjust based on your data model
    service_requests = storage.all(ServiceRequest)  # Adjust based on your data model
    equipment_listings = storage.all(EquipmentListing)  # Adjust based on your data model

    # Render the admin dashboard template with dynamic data
    return render_template('admin_dashboard.html', users=users, service_requests=service_requests, equipment_listings=equipment_listings)

if __name__ == '__main__':
    app.run(debug=True)
