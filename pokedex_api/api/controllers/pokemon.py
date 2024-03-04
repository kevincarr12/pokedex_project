from api.model.models import Pokemon, db
# from api.schema.pokemon import pokemonSchema, pokemons_schema, pokemon_schema

class pokemonController():


	def pokemon():
		session: sqlalchemy.orm.scoping.scoped_session = db.session
		pokemon = session.query(Pokemon).order_by(Pokemon.id_pokemon).all()

		return pokemon

	def getPokemon(id_pokemon):
		session: sqlalchemy.orm.scoping.scoped_session = db.session
		pokemon = session.query(Pokemon).filter(Pokemon.id_pokemon.in_([id_pokemon]))

		return pokemon

	def addPokemon(name, description):
		session: sqlalchemy.orm.scoping.scoped_session = db.session
		pokemon = Pokemon()
		if(name):
			pokemon.name = name
		if(description):
			pokemon.description = description
		db.session.add(pokemon)
		db.session.commit()

		return pokemon

	def updatePokemon(id_pokemon, name, description):
		session: sqlalchemy.orm.scoping.scoped_session = db.session
		pokemon = session.query(Pokemon).filter(Pokemon.id_pokemon == id_pokemon).update({'name':name, 'description':description})
		db.session.commit()

		return pokemon

	def deletePokemon(id_pokemon):
		session: sqlalchemy.orm.scoping.scoped_session = db.session
		pokemon = session.query(Pokemon).filter(Pokemon.id_pokemon == id_pokemon).delete()
		db.session.commit()

		return pokemon