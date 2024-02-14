#!/usr/bin/python3
"""
Contains the admin dashboard routes
"""
from flask import Flask, render_template, request, redirect, url_for
from models.feedback import Feedback, FeedbackForm
from models.storage import Storage
from datetime import datetime

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

        # Redirect to a success page or perform any other necessary action
        return redirect(url_for('feedback_success'))

    # Render the feedback form
    return render_template('feedback_form.html', form=form)

@app.route('/feedback-success')
def feedback_success():
    return render_template('feedback_success.html')

if __name__ == '__main__':
    app.run(debug=True)
