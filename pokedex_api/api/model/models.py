from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db = SQLAlchemy()

@dataclass
class Trainer(db.Model):
	__tablename__ = 'trainer'

	id_trainer:int = db.Column(db.Integer, primary_key=True)
	name:str = db.Column(db.String(100), nullable=False)
	start_date:str = db.Column(db.String(10), nullable=False)

@dataclass
class Pokemon(db.Model):
	__tablename__ = 'pokemon'

	id_pokemon:int = db.Column(db.Integer, primary_key=True)
	name:str = db.Column(db.String(50), nullable=False)
	description:str = db.Column(db.String(200), nullable=False)

@dataclass
class Pokedex(db.Model):
	__tablename__ = 'pokedex'

	id_pokedex:int = db.Column(db.Integer, primary_key=True)
	id_trainer:int = db.Column(db.Integer, nullable=False)
	id_pokemon:int = db.Column(db.Integer, nullable=False)
	catch_date:str = db.Column(db.String(10), nullable=False)