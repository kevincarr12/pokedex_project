from api.model.models import Trainer, db
from flask import jsonify

class trainerController():
	def getTrainers():
		session: sqlalchemy.orm.scoping.scoped_session = db.session
		trainers = session.query(Trainer).order_by(Trainer.id_trainer).all()

		return jsonify(trainers=trainers)
