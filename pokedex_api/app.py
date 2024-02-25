from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from datetime import date
from flasgger import swag_from
from http import HTTPStatus
from api.route.home import home_api_bp
from api.route.trainer import trainer_bp
from api.route.pokemon import pokemon_bp
from api.route.pokedex import pokedex_bp
from api.model.models import db

def createApp():
	app = Flask(__name__)
	app.register_blueprint(home_api_bp)
	app.register_blueprint(trainer_bp)
	app.register_blueprint(pokemon_bp)
	app.register_blueprint(pokedex_bp)

	app.config['MYSQL_HOST'] = 'localhost'
	app.config['MYSQL_USER'] = 'root'
	app.config['MYSQL_PASSWORD'] = 'admin'
	app.config['MYSQL_DB'] = 'pokedex'
	app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:admin@localhost/pokedex?charset=utf8'
	db.init_app(app)
	# mysql = MySQL(app)

	return app

# @app.route('/')
# def welcome():
#     routes = {
#     	'baseUrl':'localhost/',
#     	'routes':{'1':'trainer','2':'pokemon', '3':'pokedex'}
#     }
#     basicInfo = jsonify(basicInfo=routes)

#     return basicInfo

# POKEDEX SECTION

# @app.route('/pokedex', methods=['GET'])
# def getPokedex():
# 	cur = mysql.connection.cursor()
# 	cur.execute('''SELECT c.name, b.name, a.catch_date
# 		FROM pokedex a 
# 		INNER JOIN pokemon b 
# 		ON a.id_pokemon = b.id_pokemon 
# 		INNER JOIN trainer c 
# 		ON a.id_trainer = c.id_trainer 
# 		ORDER BY c.id_trainer, b.id_pokemon''')
# 	data = cur.fetchall()
# 	cur.close()

# 	return jsonify(data)

# @app.route('/pokedex', methods=['POST'])
# def setPokedex():
# 	cur = mysql.connection.cursor()
# 	id_trainer = request.json['id_trainer']
# 	id_pokemon = request.json['id_pokemon']
# 	today = date.today()
# 	d_date = today.strftime('%m-%d-%Y')
# 	cur.execute('''INSERT INTO pokedex (id_trainer, id_pokemon, catch_date) 
# 		VALUES (%s, %s, %s)''', (id_trainer, id_pokemon, d_date))
# 	mysql.connection.commit()
# 	cur.close()

# 	return jsonify({'message':'Pokemon added to the pokedex successfully'})

# @app.route('/pokedex/<int:id_pokedex>', methods=['PUT'])
# def updatePokedex(id_pokedex):
# 	cur = mysql.connection.cursor()
# 	id_trainer = request.json['id_trainer']
# 	id_pokemon = request.json['id_pokemon']
# 	today = date.today()
# 	d_date = today.strftime('%m-%d-%Y')
# 	cur.execute('''UPDATE pokedex 
# 		SET id_trainer = %s, 
# 		id_pokemon = %s, 
# 		catch_date = %s
# 		WHERE id_pokedex = %s
# 		''', (id_trainer, id_pokemon, d_date, id_pokedex))
# 	mysql.connection.commit()
# 	cur.close()

# 	return jsonify({'message':'Pokedex updated successfully'})

# @app.route('/pokedex/<int:id_pokedex>', methods=['DELETE'])
# def deletePokedex(id_pokedex):
# 	cur = mysql.connection.cursor()
# 	cur.execute('''DELETE FROM pokedex WHERE id_pokedex = %s''', (id_pokedex,))
# 	mysql.connection.commit()
# 	cur.close()

# 	return jsonify({'message':'Pokedex entry deleted successfully'})

# POKEDEX SECTION ENDS

if __name__ == '__main__':
	app.run(debug=True)

app = createApp()