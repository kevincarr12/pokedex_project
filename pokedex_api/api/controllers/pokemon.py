from api.model.models import Pokemon, db
from flask import jsonify

class pokemonController():
	def getPokemon():
		session: sqlalchemy.orm.scoping.scoped_session = db.session
		pokemon = session.query(Pokemon).order_by(Pokemon.id_pokemon).all()

		return jsonify(pokemon=pokemon)

#POKEMON SECTION

# @app.route('/pokemon', methods=['GET'])
# def getPokemons():
# 	cur = mysql.connection.cursor()
# 	cur.execute('SELECT * FROM pokemon')
# 	data = cur.fetchall()
# 	cur.close()

# 	return jsonify(data)

# @app.route('/pokemon/<int:id_pokemon>', methods=['GET'])
# def getPokemon(id_pokemon):
# 	cur = mysql.connection.cursor()
# 	cur.execute('SELECT id_pokemon, name, description FROM pokemon WHERE id_pokemon = %s',(id_pokemon,))
# 	data = cur.fetchall()
# 	cur.close()
	
# 	return jsonify(data)

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