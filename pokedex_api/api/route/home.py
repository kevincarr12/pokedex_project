from flask import Blueprint
from http import HTTPStatus
from flasgger import swag_from

home_api_bp = Blueprint('pokedex_api',__name__)

@home_api_bp.route('/')
def welcome():
	return 'Welcome to the Pokedex API by Kevin Carrasco'

