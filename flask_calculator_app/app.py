
from flask import Flask
from flask_calculator_app.home import home_bp
from flask_calculator_app.calculator import calculator_bp
from flask_calculator_app.about import about_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(home_bp)
app.register_blueprint(calculator_bp)
app.register_blueprint(about_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
