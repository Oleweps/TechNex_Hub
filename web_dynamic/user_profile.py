#!/usr/bin/python3
"""
Contains the admin dashboard routes
"""
import uuid
from flask import Flask, render_template, request, redirect, url_for
from models import storage
from models.user import User  # Import User model, adjust as needed

app = Flask(__name__)

@app.route('/user-profile', methods=['GET', 'POST'])
def user_profile():
    user_id = 1  # Replace with the actual user ID
    user = storage.get(User, user_id)

    if request.method == 'POST':
        # Update user profile based on the form data
        user.username = request.form['editUsername']
        user.email = request.form['editEmail']
        user.contact_details = request.form['editContact']
        storage.save()

        # Redirect to the user profile page after saving changes
        return redirect(url_for('user_profile'))

    # Generate a UUID (cache_id)
    cache_id = str(uuid.uuid4())

    return render_template('user_profile.html', user=user, cache_id=cache_id)

if __name__ == '__main__':
    app.run(debug=True)
