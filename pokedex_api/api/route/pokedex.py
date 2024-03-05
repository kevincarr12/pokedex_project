from flask import Blueprint, request
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
@pokedex_bp.route('/', methods=['GET'])
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
@pokedex_bp.route('/<int:id_trainer>', methods=['GET'])
def getPokedexTrainer(id_trainer):
	pokedex = pokedexController
	resultPokedex = pokedex.getPokedexTrainer(id_trainer)
	print(resultPokedex)
	return pokedexs_schema.dump(resultPokedex)

@swag_from({
	'responses': {
		HTTPStatus.OK.value: {
			'description':'Add a new Pokedex entry',
			'schema':pokedexSchema
		}
	}
})
@pokedex_bp.route('/', methods=['POST'], strict_slashes=False)
def addPokedex():
	id_trainer = request.json['id_trainer']
	id_pokemon = request.json['id_pokemon']
	catch_date = request.json['catch_date']
	pokedex = pokedexController
	newPokedex = pokedex.addPokedex(id_trainer, id_pokemon, catch_date)

	return pokedex_schema.dump(newPokedex), 201

@swag_from({
	'responses': {
		HTTPStatus.OK.value: {
			'description':'Update an existing Pokedex entry',
			'schema':pokedexSchema
		}
	}
})
@pokedex_bp.route('/<int:id_pokedex>', methods=['PUT'], strict_slashes=False)
def updatePokedex(id_pokedex):
	id_trainer = request.json['id_trainer']
	id_pokemon = request.json['id_pokemon']
	catch_date = request.json['catch_date']
	pokedex = pokedexController
	updatePokedex = pokedex.updatePokedex(id_pokedex, id_trainer, id_pokemon, catch_date)

	return pokedex_schema.dump(updatePokedex), 200

@swag_from({
	'responses': {
		HTTPStatus.OK.value: {
			'description':'Delete a Pokedex entry',
			'schema':pokedexSchema
		}
	}
})
@pokedex_bp.route('/<int:id_pokedex>', methods=['DELETE'])
def deletePokedex(id_pokedex):
	pokedex = pokedexController
	deletePokedex = pokedex.deletePokedex(id_pokedex)

	return pokedex_schema.dump(deletePokedex), 200