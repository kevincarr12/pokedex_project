from flask import Blueprint, request
from http import HTTPStatus
from flasgger import swag_from
from api.controllers.trainer import trainerController
from api.schema.trainer import trainerSchema, trainers_schema, trainer_schema

trainer_bp = Blueprint('trainer',__name__, url_prefix='/trainer')

@swag_from({
	'responses': {
		HTTPStatus.OK.value: {
			'description':'Select all Trainers',
			'schema': trainerSchema
		}
	}
})
@trainer_bp.route('/', methods=['GET'])
def trainers():
	'''
	Get All Trainers
	This method returns all the trainers registered
	'''
	tr = trainerController
	resultTrainer = tr.trainers()
	return trainers_schema.dump(resultTrainer), 200

@swag_from({
	'responses': {
		HTTPStatus.OK.value: {
			'description':'Select a specific trainer',
			'schema': trainerSchema
		}
	}
})
@trainer_bp.route('/<int:id_trainer>', methods=['GET'])
def getTrainer(id_trainer):
	'''
	Get a specific trainer
	This method returns a specific trainer called by its id_trainer
	'''
	tr = trainerController
	resultTrainer = tr.getTrainer(id_trainer)

	return trainers_schema.dump(resultTrainer), 200

@swag_from({
	'responses':{
		HTTPStatus.OK.value: {
			'message':'Add a new trainer',
			'schema': trainerSchema
		}
	}
})
@trainer_bp.route('/', methods=['POST'], strict_slashes=False)
def addTrainer():
	'''
	Add a new trainer
	Providing name and start_date('mm-dd-yyyy')
	'''
	name = request.json['name']
	start_date = request.json['start_date']
	tr = trainerController
	newTrainer = tr.addTrainer(name, start_date)

	return trainers_schema.dump(newTrainer), 201

@swag_from({
	'responses': {
		HTTPStatus.OK.value: {
			'message':'Modify an existing trainer',
			'schema':trainerSchema
		}
	}
})
@trainer_bp.route('/<int:id_trainer>', methods=['PUT'], strict_slashes=False)
def updateTrainer(id_trainer):
	'''
	Modify an existing trainer specified by the id_trainer
	Updatable fields: name, start_date
	'''
	name = request.json['name']
	start_date = request.json['start_date']
	tr = trainerController
	updateTrainer = tr.updateTrainer(id_trainer, name, start_date)

	return trainer_schema.dump(updateTrainer), 200	

@swag_from({
	'responses':{
		HTTPStatus.OK.value:{
			'message':'Delete a trainer',
			'schema':trainerSchema
		}
	}	
})
@trainer_bp.route('/<int:id_trainer>', methods=['DELETE'])
def deleteTrainer(id_trainer):
	'''
	Delete a specific trainer by its id_trainer
	'''
	trainer = trainerController
	deleteTrainer = trainer.deleteTrainer(id_trainer)

	return trainer_schema.dump(deleteTrainer), 200