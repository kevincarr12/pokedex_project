from flask import Blueprint
from http import HTTPStatus
from flasgger import swag_from
from api.controllers.pokedex import pokedexController
from api.schema.pokedex import pokedexSchema, pokedexs_schema, pokedex_schema

pokedex_bp = Blueprint('pokedex', __name__, url_prefix='/pokedex')

@swag_from({
	'responses': {
		HTTPStatus.OK.value: {
			'description':'Select all Pokemon registered on Pokedex',
			'schema': pokedexSchema
		}
	}
})
@pokedex_bp.route('/')
def getPokedex():
	pokedex = pokedexController
	resultPokedex = pokedex.getPokedex()
	return pokedexs_schema.dump(resultPokedex)

@swag_from({
	'responses': {
		HTTPStatus.OK.value: {
			'description':'Select all Pokemon registered on a Pokedex belonging to a specific trainer',
			'schema': pokedexSchema
		}
	}
})
@pokedex_bp.route('/<int:id_trainer>')
def getPokedexTrainer(id_trainer):
	pokedex = pokedexController
	resultPokedex = pokedex.getPokedexTrainer(id_trainer)
	print(resultPokedex)
	return pokedexs_schema.dump(resultPokedex)
