from flask import Blueprint

# Create a Blueprint for calculator
calculator_bp = Blueprint('calculator', __name__, static_folder='static',static_url_path='/calculator/static',template_folder='templates')

# Import routes after creating the Blueprint to avoid circular imports
from . import routes