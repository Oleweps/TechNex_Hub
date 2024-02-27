#!/usr/bin/python3
"""
Contains the admin dashboard routes
"""
from flask import Flask, render_template, request, redirect, url_for
from models.user import User, RegisterForm  # Import the RegisterForm class
from models import storage
from . import bp

app = Flask(__name__)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        contact = form.contact_details.data

        # Create a new user instance
        new_user = User(username=username, email=email, password=password, contact_details=contact)

        # Add the new user to the database
        storage.new(new_user)

        # Commit the changes to the database
        storage.save()

        # Redirect to the registration success page with the username
        return redirect(url_for('registration_success', username=username))

    # Render the registration form
    return render_template('registration_form.html', form=form)

@bp.route('/registration-success/<username>')
def registration_success(username):
    return render_template('registration_success.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
