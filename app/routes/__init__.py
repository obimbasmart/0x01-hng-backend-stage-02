"""
    application index blueprint
"""

from flask import Blueprint

api_routes = Blueprint('api_routes', url_prefix="/api", import_name=__name__)

from . import index