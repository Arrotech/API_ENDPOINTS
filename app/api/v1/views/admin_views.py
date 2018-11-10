from flask_restful import Resource
from flask import make_response, jsonify, request, Blueprint, abort
from app.api.v1.models.models import ParcelModel


parcel_v1 = Blueprint('v1',__name__)

class DataParcel(Resource):
	def __init__(self):
		pass 

	@parcel_v1.route('',methods=['POST'])
	def create_order():
		if not request.json or not 'sender_name' in request.json:
			abort(400)
		if not request.json or not 'recipient' in request.json:
			abort(400)
		if not request.json or not 'destination' in request.json:
			abort(400)
		if not request.json or not 'pickup' in request.json:
			abort(400)
		if not request.json or not 'weight' in request.json:
			abort(400)
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
	def get_parcels():
		parcels = ParcelModel().get_all_parcels()
		return make_response(jsonify({
			"Message": "Hurray! It worked!!!",
			"Parcel Order": ParcelModel().get_all_parcels()
			}),201)


	@parcel_v1.route('/<int:parcel_id>',methods=['GET'])
	def get_parcel(parcel_id):
		Order = ParcelModel().get_parcel_by_id(parcel_id)

		return make_response(jsonify({
			"Message": "Hurray! It worked!!!",
			"Parcel Order": Order
			}),201)

	'''@parcel_v1.route('<int:parcel_id>', methods=['DELETE'])
	def cancel_order(self, parcel_id):
		order = ParcelModel().get_parcel_by_id(self, parcel_id)
		if order:
			ParcelModel().cancel_order_by_id(self, parcel_id)
			return jsonify({'Message': 'Order cancelled'}), 200'''





