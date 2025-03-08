from flask import Blueprint

# Create a Blueprint for home
home_bp = Blueprint('home', __name__, static_folder='static', template_folder='templates')

# Import routes after creating the Blueprint to avoid circular imports
from . import routes