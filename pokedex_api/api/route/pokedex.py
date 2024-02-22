from flask import Blueprint
from http import HTTPStatus
from flasgger import swag_from
from api.controllers.pokedex import pokedexController

pokedex_bp = Blueprint('pokedex', __name__, url_prefix='/pokedex')

@pokedex_bp.route('/')
def getPokedex():
	pokedex = pokedexController
	return pokedex.getPokedex()

@pokedex_bp.route('/<int:id_trainer>')
def getPokedexTrainer(id_trainer):
	pokedex = pokedexController
	return pokedex.getPokedexTrainer(id_trainer)
