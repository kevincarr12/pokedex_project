from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from datetime import date

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'pokedex'
mysql = MySQL(app) 

@app.route('/')
def welcome():
    routes = {
    	'baseUrl':'localhost/',
    	'routes':{'1':'trainer','2':'pokemon', '3':'pokedex'}
    }
    basicInfo = jsonify(basicInfo=routes)

    return basicInfo

# TRAINER SECTION
@app.route('/trainer', methods=['GET'])
def getTrainers():
	cur = mysql.connection.cursor()
	cur.execute('SELECT * FROM trainer')
	data = cur.fetchall()
	cur.close()

	return jsonify(data)

@app.route('/trainer/<int:id_trainer>', methods=['GET'])
def getTrainer(id_trainer):
	cur = mysql.connection.cursor()
	cur.execute('SELECT id_trainer, name, start_date FROM trainer WHERE id_trainer = %s', (id_trainer,))
	data = cur.fetchall()
	cur.close()

	return jsonify(data)

@app.route('/trainer', methods=['POST'])
def setTrainer():
	cur = mysql.connection.cursor()
	name = request.json['name']
	start_date  = request.json['start_date']
	cur.execute('INSERT INTO trainer (name, start_date) VALUES (%s, %s)', (name, start_date,))
	mysql.connection.commit()
	cur.close()
	
	return jsonify({'message':'Trainer created successfully'})

@app.route('/trainer/<int:id_trainer>', methods=['PUT'])
def updateTrainer(id_trainer):
	cur  = mysql.connection.cursor()
	name = request.json['name']
	start_date = request.json['start_date']
	cur.execute('UPDATE trainer SET name = %s, start_date = %s WHERE id_trainer = %s', (name, start_date, id_trainer,))
	mysql.connection.commit()
	cur.close()

	return jsonify({'message':'Trainer updated successfully'})

@app.route('/trainer/<int:id_trainer>', methods=['DELETE'])
def deleteTrainer(id_trainer):
	return jsonify({'message':'Method under work'})

# TRAINER SECTION ENDS

#POKEMON SECTION

@app.route('/pokemon', methods=['GET'])
def getPokemons():
	cur = mysql.connection.cursor()
	cur.execute('SELECT * FROM pokemon')
	data = cur.fetchall()
	cur.close()

	return jsonify(data)

@app.route('/pokemon/<int:id_pokemon>', methods=['GET'])
def getPokemon(id_pokemon):
	cur = mysql.connection.cursor()
	cur.execute('SELECT id_pokemon, name, description FROM pokemon WHERE id_pokemon = %s',(id_pokemon,))
	data = cur.fetchall()
	cur.close()
	
	return jsonify(data)

@app.route('/pokemon', methods=['POST'])
def setPokemon():
	cur = mysql.connection.cursor()
	name = request.json['name']
	description  = request.json['description']
	cur.execute('INSERT INTO pokemon (name, description) VALUES (%s, %s)', (name, description,))
	mysql.connection.commit()
	cur.close()
	
	return jsonify({'message':'Pokemon created successfully'})

@app.route('/pokemon/<int:id_pokemon>', methods=['PUT'])
def updatePokemon(id_pokemon):
	cur  = mysql.connection.cursor()
	name = request.json['name']
	description = request.json['description']
	cur.execute('UPDATE pokemon SET name = %s, description = %s WHERE id_pokemon = %s', (name, description, id_pokemon,))
	mysql.connection.commit()
	cur.close()

	return jsonify({'message':'Pokemon updated successfully'})

@app.route('/pokemon/<int:id_pokemon>', methods=['DELETE'])
def deletePokemon(id_pokemon):
	return jsonify({'message':'Method under work'})

# POKEMON SECTION ENDS

# POKEDEX SECTION

@app.route('/pokedex', methods=['GET'])
def getPokedex():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT c.name, b.name, a.catch_date
		FROM pokedex a 
		INNER JOIN pokemon b 
		ON a.id_pokemon = b.id_pokemon 
		INNER JOIN trainer c 
		ON a.id_trainer = c.id_trainer 
		ORDER BY c.id_trainer, b.id_pokemon''')
	data = cur.fetchall()
	cur.close()

	return jsonify(data)

@app.route('/pokedex', methods=['POST'])
def setPokedex():
	cur = mysql.connection.cursor()
	id_trainer = request.json['id_trainer']
	id_pokemon = request.json['id_pokemon']
	today = date.today()
	d_date = today.strftime('%m-%d-%Y')
	cur.execute('''INSERT INTO pokedex (id_trainer, id_pokemon, catch_date) 
		VALUES (%s, %s, %s)''', (id_trainer, id_pokemon, d_date))
	mysql.connection.commit()
	cur.close()

	return jsonify({'message':'Pokemon added to the pokedex successfully'})

@app.route('/pokedex/<int:id_pokedex>', methods=['PUT'])
def updatePokedex(id_pokedex):
	cur = mysql.connection.cursor()
	id_trainer = request.json['id_trainer']
	id_pokemon = request.json['id_pokemon']
	today = date.today()
	d_date = today.strftime('%m-%d-%Y')
	cur.execute('''UPDATE pokedex 
		SET id_trainer = %s, 
		id_pokemon = %s, 
		catch_date = %s
		WHERE id_pokedex = %s
		''', (id_trainer, id_pokemon, d_date, id_pokedex))
	mysql.connection.commit()
	cur.close()

	return jsonify({'message':'Pokedex updated successfully'})

@app.route('/pokedex/<int:id_pokedex>', methods=['DELETE'])
def deletePokedex(id_pokedex):
	return jsonify({'message':'Method under work'})

# POKEDEX SECTION ENDS

if __name__ == '__main__':
	app.run(debug=True)

