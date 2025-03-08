from flask import Blueprint

# Create a Blueprint for about
about_bp = Blueprint('about', __name__, static_folder='static',static_url_path='/about/static', template_folder='templates')

# Import routes after creating the Blueprint to avoid circular imports
from . import routes