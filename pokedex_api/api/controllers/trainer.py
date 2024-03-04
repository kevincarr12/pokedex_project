from api.model.models import Trainer, db
# from api.schema.trainer import trainerSchema, trainers_schema, trainer_schema

class trainerController():
	def trainers():
		session: sqlalchemy.orm.scoping.scoped_session = db.session
		trainers = session.query(Trainer).order_by(Trainer.id_trainer).all()

		return trainers

	def getTrainer(id_trainer):
		session: sqlalchemy.orm.scoping.scoped_session = db.session
		trainer = session.query(Trainer).filter(Trainer.id_trainer.in_([id_trainer]))

		return trainer

	def addTrainer(name, start_date):
		session: sqlalchemy.orm.scoping.scoped_session = db.session
		trainer = Trainer()
		if(name):
			trainer.name = name
		if(start_date):
			trainer.start_date = start_date
		db.session.add(trainer)
		db.session.commit()

	def updateTrainer(id_trainer, name, start_date):
		session: sqlalchemy.orm.scoping.scoped_session = db.session
		trainer = session.query(Trainer).filter(Trainer.id_trainer == id_trainer).update({'name':name, 'start_date':start_date})
		db.session.commit()

		return trainer

	def deleteTrainer(id_trainer):
		session: sqlalchemy.orm.scoping.scoped_session = db.session
		trainer = session.query(Trainer).filter(Trainer.id_trainer == id_trainer).delete()
		db.session.commit()

		return trainer
