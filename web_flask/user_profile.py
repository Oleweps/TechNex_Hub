#!/usr/bin/python3
"""
Contains the admin dashboard routes
"""
from flask import Flask, render_template, request, redirect, url_for
from models.storage import Storage

app = Flask(__name__)
storage = Storage()

@app.route('/user-profile', methods=['GET', 'POST'])
def user_profile():
    user = storage.get('User', 1)  # Replace 1 with the actual user ID

    if request.method == 'POST':
        # Update user profile based on the form data
        user.username = request.form['editUsername']
        user.email = request.form['editEmail']
        user.contact_details = request.form['editContact']
        storage.save()

        # Redirect to the user profile page after saving changes
        return redirect(url_for('user_profile'))

    return render_template('user_profile.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
