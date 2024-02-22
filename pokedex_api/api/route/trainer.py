from flask import Blueprint
from http import HTTPStatus
from flasgger import swag_from
from api.controllers.trainer import trainerController

trainer_bp = Blueprint('trainer',__name__, url_prefix='/trainer')

@trainer_bp.route('/')
def trainers():
	tr = trainerController
	return tr.getTrainers()

# TRAINER SECTION
# @app.route('/trainer', methods=['GET'])
# def getTrainers():
# 	cur = mysql.connection.cursor()
# 	cur.execute('SELECT * FROM trainer')
# 	data = cur.fetchall()
# 	cur.close()

# 	return jsonify(data)

# @app.route('/trainer/<int:id_trainer>', methods=['GET'])
# def getTrainer(id_trainer):
# 	cur = mysql.connection.cursor()
# 	cur.execute('SELECT id_trainer, name, start_date FROM trainer WHERE id_trainer = %s', (id_trainer,))
# 	data = cur.fetchall()
# 	cur.close()

# 	return jsonify(data)

# @app.route('/trainer', methods=['POST'])
# def setTrainer():
# 	cur = mysql.connection.cursor()
# 	name = request.json['name']
# 	start_date  = request.json['start_date']
# 	cur.execute('INSERT INTO trainer (name, start_date) VALUES (%s, %s)', (name, start_date,))
# 	mysql.connection.commit()
# 	cur.close()
	
# 	return jsonify({'message':'Trainer created successfully'})

# @app.route('/trainer/<int:id_trainer>', methods=['PUT'])
# def updateTrainer(id_trainer):
# 	cur  = mysql.connection.cursor()
# 	name = request.json['name']
# 	start_date = request.json['start_date']
# 	cur.execute('UPDATE trainer SET name = %s, start_date = %s WHERE id_trainer = %s', (name, start_date, id_trainer,))
# 	mysql.connection.commit()
# 	cur.close()

# 	return jsonify({'message':'Trainer updated successfully'})

# @app.route('/trainer/<int:id_trainer>', methods=['DELETE'])
# def deleteTrainer(id_trainer):
# 	cur = mysql.connection.cursor()
# 	cur.execute('''DELETE FROM trainer WHERE id_trainer =  %s''', (id_trainer,))
# 	cur.connection.commit()
# 	cur.close()

# 	return jsonify({'message':'Trainer deleted successfully'})

# TRAINER SECTION ENDS

