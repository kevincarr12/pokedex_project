from api.model.models import Trainer, db

class trainerController():
	def trainers():
		session: sqlalchemy.orm.scoping.scoped_session = db.session
		trainers = session.query(Trainer).order_by(Trainer.id_trainer).all()

		return trainers

	def getTrainer(id_trainer):
		session: sqlalchemy.orm.scoping.scoped_session = db.session
		trainer = session.query(Trainer).filter(Trainer.id_trainer.in_([id_trainer]))

		return trainer
