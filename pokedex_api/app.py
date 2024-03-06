from configparser import ConfigParser
from flask import Flask
# , jsonify, request
# from flask_mysqldb import MySQL
# from datetime import date
# from flasgger import swag_from
# from http import HTTPStatus
from api.route.home import home_api_bp
from api.route.trainer import trainer_bp
from api.route.pokemon import pokemon_bp
from api.route.pokedex import pokedex_bp
from api.model.models import db

config = ConfigParser()
configFile = 'config.ini'
config.read(configFile)

def createApp():
	app = Flask(__name__)
	app.register_blueprint(home_api_bp)
	app.register_blueprint(trainer_bp)
	app.register_blueprint(pokemon_bp)
	app.register_blueprint(pokedex_bp)

	app.config['MYSQL_HOST'] = config.get('mysql','host')
	app.config['MYSQL_USER'] = config.get('mysql','user')
	app.config['MYSQL_PASSWORD'] = config.get('mysql','password')
	app.config['MYSQL_DB'] = config.get('mysql','db')
	app.config['SQLALCHEMY_DATABASE_URI']=config.get('sqlalchemy','database_uri')
	db.init_app(app)

	return app

if __name__ == '__main__':
	app.run()

app = createApp()