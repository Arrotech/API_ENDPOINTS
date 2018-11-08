from flask_restful import Resource
from flask import make_response, jsonify, request, Blueprint
from models import ParcelModel

parcel_v1 = Blueprint('v1',__name__)
parcel = ParcelModel()
"""par = ParcelModel().get_all_orders()"""

class DataParcel(Resource):

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


		parcel.save(sender_name,recipient,destination,pickup,weight)
		return make_response(jsonify({
			"Message": "Hurray! It worked!!!"
			}),201)