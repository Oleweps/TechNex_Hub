#!/usr/bin/python3
"""
Contains the admin dashboard routes
"""
from flask import Flask, render_template, request, redirect, url_for
from models import storage
from models.notification import Notification
from . import bp

app = Flask(__name__)

@bp.route('/notifications-center', methods=['GET', 'POST'])
def notifications_center():
    if request.method == 'POST':
        # Clear all notifications (you may want to implement more specific logic)
        storage.delete_all(Notification)
        storage.save()

    # Get notifications from storage
    notifications = storage.all(Notification).values()

    return render_template('notifications_center.html', notifications=notifications)

if __name__ == '__main__':
    app.run(debug=True)
