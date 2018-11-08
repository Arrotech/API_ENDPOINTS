from flask_restful import Resource
from flask import make_response, jsonify, request, Blueprint
from app.api.v1.models.models import ParcelModel

parcel_v1 = Blueprint('v1',__name__)

class DataParcel(Resource):
	def __init__(self):
		pass 

	@parcel_v1.route('',methods=['POST'])
	def post():
		# if not request.json or not 'sender_name' in request.json:
		# 	abort(400)
		details = request.get_json()

		sender_name = details['sender_name'],
		recipient = details['recipient'],
		destination = details['destination'],
		pickup = details['pickup'],
		weight = details['weight']


		res = ParcelModel().save(sender_name,recipient,destination,pickup,weight)

		return make_response(jsonify({
			"Message": "Hurray! It worked!!!",
			"Parcel Order": res
			}),201)

	@parcel_v1.route('',methods=['GET'])
	def get():
		parcels = ParcelModel().get_all_parcels()
		return make_response(jsonify({
			"Message": "Hurray! It worked!!!",
			"Parcel Order": ParcelModel().get_all_parcels()
			}),201)




