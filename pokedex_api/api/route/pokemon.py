from flask import Blueprint
from http import HTTPStatus
from flasgger import swag_from
from api.controllers.pokemon import pokemonController

pokemon_bp = Blueprint('pokemon', __name__, url_prefix='/pokemon')

@pokemon_bp.route('/')
def pokemon():
	pokemon = pokemonController
	return pokemon.getPokemon()
