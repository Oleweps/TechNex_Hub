#!/usr/bin/python3
"""
Contains the admin dashboard routes
"""
from flask import Flask, render_template, redirect, url_for, session, request
from models.auth_token import AuthenticationToken
from models.storage import Storage
from models.user import LogoutForm, User  # Import the LogoutForm class

app = Flask(__name__)
app.secret_key = 'e240d6581e46733f46bc422ae81d9776'  # Replace with a secure secret key
storage = Storage()

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    form = LogoutForm()

    if request.method == 'POST' and form.validate_on_submit():
        # Remove user's information from the session
        session.pop('user_id', None)
        session.pop('token', None)

        # Delete the authentication token from the database
        user_id = form.user_id.data
        token = form.token.data
        storage.delete(AuthenticationToken(user_id=user_id, token=token))
        storage.save()

        return redirect(url_for('home'))

    # Render the logout confirmation form
    return render_template('logout.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
