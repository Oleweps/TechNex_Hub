#!/usr/bin/python3
"""
This is the views package for API version 1.
"""

from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


from api.v1.views.index import *
from api.v1.views.user import *
from api.v1.views.service_request import *
from api.v1.views.service import *
from api.v1.views.equipment_listing import *
from api.v1.views.message import *
from api.v1.views.authentication_token import *
from api.v1.views.feedback import *
from api.v1.views.suggestion import *
from api.v1.views.admin import *
from api.v1.views.notifications import *
