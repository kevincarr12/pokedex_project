from flask import jsonify
from api.model.models import db, Pokedex

class pokedexController():
	def getPokedex():
		session: sqlalchemy.orm.scoping.scoped_session = db.session
		pokedex = session.query(Pokedex).order_by(Pokedex.id_pokedex).all()

		return jsonify(pokedex=pokedex)

	def getPokedexTrainer(id_trainer):
		session: sqlalchemy.orm.scoping.scoped_session = db.session
		pokedex = session.query(Pokedex).filter(Pokedex.id_trainer.in_([id_trainer])).all()

		return jsonify(pokedex=pokedex)