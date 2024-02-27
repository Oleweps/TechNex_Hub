#!/usr/bin/python3
"""
Contains the admin dashboard routes
"""
from flask import Flask, render_template, request, redirect, url_for
from models.message import Message, MessageForm
from models import storage
from datetime import datetime
from . import bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e240d6581e46733f46bc422ae81d9776'  # Replace with a secure secret key

@bp.route('/send-message', methods=['GET', 'POST'])
def send_message():
    form = MessageForm()

    if request.method == 'POST' and form.validate_on_submit():
        # Get message data from the form
        receiver_id = form.receiver_id.data
        content = form.content.data
        timestamp = datetime.now()

        # Assume you have the sender_id, adjust accordingly
        sender_id = "sender_id_here"

        # Create a Message object
        message = Message(sender_id=sender_id, receiver_id=receiver_id,
                          timestamp=timestamp, content=content)

        # Add the message to the database and save changes
        storage.new(message)
        storage.save()

        # Redirect to a success page or perform any other necessary action
        return redirect(url_for('message_success'))

    # Render the message form
    return render_template('message_form.html', form=form)

@bp.route('/message-success')
def message_success():
    return render_template('message_success.html')

if __name__ == '__main__':
    app.run(debug=True)
