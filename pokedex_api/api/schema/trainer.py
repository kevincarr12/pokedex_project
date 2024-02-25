from flask_marshmallow import Schema
from marshmallow.fields import Str

class trainerSchema(Schema):
	class Meta:
		fields = ["id_trainer","name","start_date"]

trainer_schema = trainerSchema()
trainers_schema = trainerSchema(many=True)
