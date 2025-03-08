from flask import Flask
from home import home_bp
from calculator import calculator_bp
from about import about_bp
from flask_calculator_app.app import app

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(home_bp)
app.register_blueprint(calculator_bp)
app.register_blueprint(about_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)