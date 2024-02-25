from flask_marshmallow import Schema
from marshmallow.fields import Str

class pokedexSchema(Schema):
	class Meta:
		fields = ["id_pokedex","id_pokemon","id_trainer","catch_date"]

pokedex_schema = pokedexSchema()
pokedexs_schema = pokedexSchema(many=True)