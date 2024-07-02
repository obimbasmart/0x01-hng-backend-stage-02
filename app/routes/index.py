"""
    index routes
"""
from app.routes import api_routes
from flask import jsonify, request
import requests
import os
import dotenv
from typing import Tuple

dotenv.load_dotenv()


def get_client_coord(ip: str) -> Tuple[str]:
    """get long and lat"""
    api_key = os.getenv('GEO_API_KEY')
    url = f"https://api.geoapify.com/v1/ipinfo?ip={ip}&apiKey={api_key}"
    res = requests.get(url).json()
    return res['location']['longitude'], res['location']['latitude']


def get_client_metadata(longitude: str, latitude: str) -> str:
    api_key = os.getenv('API_KEY')
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
    res = requests.get(url).json()
    return res['name'], res['main']['temp']


@api_routes.route("/hello")
def greet():
    ip = request.headers.get('X-Real-IP')
    visitor_name = request.args.get("visitor_name")
    longitude, latitude = get_client_coord(ip)

    city, temp = get_client_metadata(longitude, latitude)

    return jsonify({
        "client_ip": ip,
        "location": city,
        "greeting": f"Hello, {visitor_name}!, the temperature is {temp} degrees Celcius in {city}"
    })
