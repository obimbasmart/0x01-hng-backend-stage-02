"""
    Simple flask app
"""

from flask import Flask
from app.routes import api_routes

def create_app():
    """app factory function"""
    app = Flask(__name__)
    app.register_blueprint(api_routes)
    app.url_map.strict_slashes = False

    return app