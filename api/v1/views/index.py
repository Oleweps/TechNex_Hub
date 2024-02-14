#!/usr/bin/python3
"""
This is the module for API version 1's index view.
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.user import User
from models.service_request import ServiceRequest
from models.service import Service
from models.equipment_listing import EquipmentListing
from models.message import Message
from models.authentication_token import AuthenticationToken
from models.feedback import Feedback
from models.suggestion import Suggestion
from models.admin import Admin
from models.notification import Notification


@app_views.route('/status', methods=['GET'])
def status():
    """
    Return a JSON response with the status.
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def object_stats():
    """
    Retrieve the number of each object by type.
    """

    objects = {
        'users': User,
        'service_requests': ServiceRequest,
        'services': Service,
        'equipment_listings': EquipmentListing,
        'messages': Message,
        'authentication_token': AuthenticationToken,
        'feedbacks': Feedback,
        'suggestions': Suggestion,
        'admins': Admin,
        'notifications': Notification,
    }
    
    for key, value in objects.items():
        objects[key] = storage.count(value)
    
    return jsonify(objects)
