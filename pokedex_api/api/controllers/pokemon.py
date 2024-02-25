from api.model.models import Pokemon, db
from api.schema.pokemon import pokemonSchema, pokemons_schema, pokemon_schema

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
		pokemon.name = name
		pokemon.description = description
		db.session.add(pokemon)
		db.session.commit()

		return pokemon

#POKEMON SECTION

# @app.route('/pokemon', methods=['POST'])
# def setPokemon():
# 	cur = mysql.connection.cursor()
# 	name = request.json['name']
# 	description  = request.json['description']
# 	cur.execute('INSERT INTO pokemon (name, description) VALUES (%s, %s)', (name, description,))
# 	mysql.connection.commit()
# 	cur.close()
	
# 	return jsonify({'message':'Pokemon created successfully'})

# @app.route('/pokemon/<int:id_pokemon>', methods=['PUT'])
# def updatePokemon(id_pokemon):
# 	cur  = mysql.connection.cursor()
# 	name = request.json['name']
# 	description = request.json['description']
# 	cur.execute('UPDATE pokemon SET name = %s, description = %s WHERE id_pokemon = %s', (name, description, id_pokemon,))
# 	mysql.connection.commit()
# 	cur.close()

# 	return jsonify({'message':'Pokemon updated successfully'})

# @app.route('/pokemon/<int:id_pokemon>', methods=['DELETE'])
# def deletePokemon(id_pokemon):
# 	cur = mysql.connection.cursor()
# 	cur.execute('''DELETE FROM pokemon WHERE id_pokemon = %s''',(id_pokemon,))
# 	mysql.connection.commit()
# 	cur.close()

# 	return jsonify({'message':'Pokemon deleted successfully'})

# POKEMON SECTION ENDS