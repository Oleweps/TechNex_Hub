#!/usr/bin/python3
"""
Contains the admin dashboard routes
"""
import uuid
from flask import Flask, render_template, request, redirect, url_for
from models.service_request import ServiceRequest, ServiceRequestForm
from models.storage import Storage

app = Flask(__name__)
app.secret_key = 'e240d6581e46733f46bc422ae81d9776'  # Replace with a secure secret key
storage = Storage()

# ... (other routes)

@app.route('/service_request_form', methods=['GET', 'POST'])
def service_request_form():
    form = ServiceRequestForm()

    if form.validate_on_submit():
        # Assuming you have a user_id available (you need to set it based on the current user)
        user_id = "user_id_here"

        # Create a new ServiceRequest object and add it to the database
        new_service_request = ServiceRequest(
            user_id=user_id,
            service_type=form.service_type.data,
            equipment_details=form.equipment_details.data,
            user_comments=form.user_comments.data
        )
        storage.new(new_service_request)
        storage.save()

        # Generate a UUID (cache_id)
        cache_id = str(uuid.uuid4())

        return redirect(url_for('service_request_success', cache_id=cache_id))

    # Generate a UUID (cache_id)
    cache_id = str(uuid.uuid4())

    return render_template('service_request_form.html', form=form, cache_id=cache_id)

@app.route('/service_request_success')
def service_request_success():
    return render_template('service_request_success.html')

if __name__ == '__main__':
    app.run(debug=True)
