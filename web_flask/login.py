#!/usr/bin/python3
"""
Contains the admin dashboard routes
"""
from flask import Flask, render_template, request, redirect, url_for, session, flash
from models.user import User, UserForm
from models.authentication_token import AuthenticationToken
from models import storage
from datetime import datetime, timedelta
import uuid
from . import bp

app = Flask(__name__)
app.secret_key = 'e240d6581e46733f46bc422ae81d9776'  # Make sure to use quotes around the secret key

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = UserForm()  # Create an instance of the UserForm

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

            return redirect(url_for('home'))
        else:
            flash('Invalid email or password. Please try again.', 'error')

    return render_template('login.html', form=form)

@bp.route('/home')
def home():
    # Replace the following with your authorization logic
    if 'user_id' in session and 'token' in session:
        return f'Welcome, User ID: {session["user_id"]}, Token: {session["token"]}'
    else:
        return 'You are not logged in'

if __name__ == '__main__':
    app.run(debug=True)
