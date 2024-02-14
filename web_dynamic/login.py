#!/usr/bin/python3
"""
Contains the admin dashboard routes
"""
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from models.user import User, UserForm
from models.authentication_token import AuthenticationToken
from models.storage import Storage
from datetime import datetime, timedelta
import uuid

app = Flask(__name__)
storage = Storage()
app.secret_key = 'e240d6581e46733f46bc422ae81d9776'

# You can generate the cache_id wherever it is convenient for you
# For example, you can generate it at the beginning of the script
cache_id = str(uuid.uuid4())

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = UserForm()

    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        # Replace the following with your actual authentication logic
        user = storage.get(User, {'email': email, 'password': password})

        if user:
            # Generate an authentication token (for demonstration purposes)
            token = str(uuid.uuid4())
            expiration_time = datetime.now() + timedelta(hours=1)

            # Save the authentication token to the database
            auth_token = AuthenticationToken(user_id=user.id, token=token, expiration_time=expiration_time)
            storage.new(auth_token)
            storage.save()

            # Set the user_id and token in the session
            session['user_id'] = user.id
            session['token'] = token

            return jsonify({'message': 'Login successful', 'redirect_url': url_for('home')})
        else:
            return jsonify({'message': 'Invalid email or password'})

    # Pass the cache_id as a context variable
    return render_template('login.html', form=form, cache_id=cache_id)

# Your other routes and configurations

if __name__ == '__main__':
    app.run(debug=True)
