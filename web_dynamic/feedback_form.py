#!/usr/bin/python3
"""
Contains the feedback routes
"""
from flask import Flask, render_template, request, redirect, url_for, jsonify
from models.feedback import Feedback, FeedbackForm
from models.storage import Storage
from datetime import datetime
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e240d6581e46733f46bc422ae81d9776'  # Replace with a secure secret key
storage = Storage()

@app.route('/feedback-form', methods=['GET', 'POST'])
def feedback_form():
    form = FeedbackForm()

    if request.method == 'POST' and form.validate_on_submit():
        # Get feedback data from the form
        ratings = form.rating.data
        comments = form.comments.data
        timestamp = datetime.now()

        # Assuming you have the user_id and technician_id, adjust accordingly
        user_id = "user_id_here"
        technician_id = "technician_id_here"

        # Create a Feedback object
        feedback = Feedback(user_id=user_id, technician_id=technician_id,
                            rating=ratings, comments=comments, timestamp=timestamp)

        # Add the feedback to the database and save changes
        storage.new(feedback)
        storage.save()

        # Generate a UUID as the cache_id
        cache_id = str(uuid.uuid4())

        # Return a success response with cache_id
        return jsonify({'success': True, 'message': 'Feedback submitted successfully', 'cache_id': cache_id})

    # Generate a UUID as the cache_id
    cache_id = str(uuid.uuid4())

    # Render the feedback form with cache_id
    return render_template('feedback_form.html', form=form, cache_id=cache_id)

@app.route('/feedback-success')
def feedback_success():
    return render_template('feedback_success.html')

if __name__ == '__main__':
    app.run(debug=True)
