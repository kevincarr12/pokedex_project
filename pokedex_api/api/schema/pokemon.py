from flask_marshmallow import Schema
from marshmallow.fields import Str

class pokemonSchema(Schema):
	class Meta:
		# fields to expose
		fields = ('id_pokemon','name','description')


pokemon_schema = pokemonSchema()
pokemons_schema = pokemonSchema(many=True)