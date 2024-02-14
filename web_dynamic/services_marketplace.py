#!/usr/bin/python3
"""
Contains the admin dashboard routes
"""
import uuid
from flask import Flask, render_template, request, jsonify
from models.storage import Storage
from models.service import Service

app = Flask(__name__)
storage = Storage()

@app.route('/services-marketplace')
def services_marketplace():
    services = storage.all(Service).values()

    # Generate a UUID (cache_id)
    cache_id = str(uuid.uuid4())

    return render_template('services_marketplace.html', services=services, cache_id=cache_id)

@app.route('/request-service', methods=['POST'])
def request_service():
    if request.method == 'POST':
        service_id = request.form.get('service_id')

        # Fetch service details from the database based on service_id
        service = storage.get(Service, id=service_id)

        # You can now implement the logic to handle the service request
        # For demonstration purposes, we'll just return a success message with service details
        response_data = {
            'message': 'Service requested successfully',
            'service_name': service.name,
            'service_description': service.description,
            'service_cost': service.cost,
        }
        return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
