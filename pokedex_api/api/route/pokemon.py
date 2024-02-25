from flask import Blueprint, request
from http import HTTPStatus
from flasgger import swag_from
from api.controllers.pokemon import pokemonController
from api.schema.pokemon import pokemonSchema, pokemons_schema, pokemon_schema

pokemon_bp = Blueprint('pokemon', __name__, url_prefix='/pokemon')


@swag_from({
	'responses': {
		HTTPStatus.OK.value: {
			'description':'List All Pokemon',
			'schema': pokemonSchema
		}
	}
})
@pokemon_bp.route('/', methods=['GET'])
def pokemon():
	'''
	Get all Pokemon
	This method returns all registered Pokemon
	'''
	pokemon = pokemonController
	allPokemon = pokemon.pokemon()
	return pokemons_schema.dump(allPokemon), 200

@swag_from({
	'responses': {
		HTTPStatus.OK.value: {
			'description':'Select a Pokemon',
			'schema': pokemonSchema
		}
	}
})
@pokemon_bp.route('/<int:id_pokemon>', methods=['GET'])
def getPokemon(id_pokemon):
	'''
	Get one Pokemon
	This method returns a specified registered Pokemon
	'''
	pokemon = pokemonController
	onePokemon = pokemon.getPokemon(id_pokemon)
	return pokemons_schema.dump(onePokemon), 200

@swag_from({
	'responses': {
		HTTPStatus.OK.value: {
			'description':'Insert a Pokemon',
			'schema':pokemonSchema
		}
	}
})
@pokemon_bp.route('/', methods=['POST'], strict_slashes=False)
def addPokemon():
	name = request.json['name']
	description = request.json['description']
	pokemon = pokemonController
	newPokemon = pokemon.addPokemon(name, description)

	return pokemon_schema.dump(newPokemon), 201