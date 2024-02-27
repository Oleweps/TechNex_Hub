from flask import Blueprint

bp = Blueprint('main', __name__)

from . import admin_dashboard
from . import equipment_listings_marketplace
from . import feedback_form
from . import login
from . import logout
from . import messaging_interface
from . import notifications
from . import register
from . import service_request_form
from . import service_marketplace
from . import suggestions
from . import user_profile