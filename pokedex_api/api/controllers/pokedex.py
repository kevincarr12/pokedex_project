from api.model.models import db, Pokedex

class pokedexController():
	def getPokedex():
		session: sqlalchemy.orm.scoping.scoped_session = db.session
		pokedex = session.query(Pokedex).order_by(Pokedex.id_pokedex).all()

		return pokedex

	def getPokedexTrainer(id_trainer):
		session: sqlalchemy.orm.scoping.scoped_session = db.session
		pokedex = session.query(Pokedex).filter(Pokedex.id_trainer.in_([id_trainer])).all()

		return pokedex

	def addPokedex(id_trainer, id_pokemon, catch_date):
		session: sqlalchemy.orm.scoping.scoped_session = db.session
		pokedex = Pokedex()
		pokedex.id_trainer = id_trainer
		pokedex.id_pokemon = id_pokemon
		pokedex.catch_date = catch_date
		db.session.add(pokedex)
		db.session.commit()

		return pokedex

	def updatePokedex(id_pokedex, id_trainer, id_pokemon, catch_date):
		session: sqlalchemy.orm.scoping.scoped_session = db.session
		pokedex = session.query(Pokedex).filter(Pokedex.id_pokedex == id_pokedex).\
				update({'id_trainer':id_trainer,'id_pokemon':id_pokemon,'catch_date':catch_date})
		db.session.commit()

		return pokedex

	def deletePokedex(id_pokedex):
		session: sqlalchemy.orm.scoping.scoped_session = db.session
		pokedex = session.query(Pokedex).filter(Pokedex.id_pokedex == id_pokedex).delete()
		db.session.commit()

		return pokedex