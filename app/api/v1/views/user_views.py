from flask_restful import Resource
from flask import make_response, jsonify, request, Blueprint, abort
from app.api.v1.models.models import ParcelModel


parcel_v1 = Blueprint('v1',__name__, url_prefix='/api/v1/')


class DataParcel(Resource):
	def __init__(self):
		pass 

	@parcel_v1.route('/parcels',methods=['POST'])
	def post():
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
		if not request.json or not 'username' in request.json:
			abort(400)
		details = request.get_json()



		sender_name = details['sender_name']
		recipient = details['recipient']
		destination = details['destination']
		pickup = details['pickup']
		weight = details['weight']
		username = details['username']

		res = ParcelModel().save(sender_name,recipient,destination,pickup,weight,username)
		return make_response(jsonify({
			"Message": "Hurray! It worked!!!",
			"Parcel Order": res
			}),201)

	@parcel_v1.route('/parcels',methods=['GET'])
	def get_parcels():
		orders = ParcelModel().get_all_parcels()
		return make_response(jsonify({
			"Message": "Hurray! It worked!!!",
			"Parcel Order": orders
			}),200)

	@parcel_v1.route('/parcels/<int:parcel_id>',methods=['GET'])
	def get_parcel(parcel_id):
		order = ParcelModel().get_parcel_by_id(parcel_id)
		return make_response(jsonify({
			"Message": "Hurray! It worked!!!",
			"Parcel Order": order
			}),200)
		
	@parcel_v1.route('/parcels/<int:parcel_id>/cancel', methods=['PUT'])
	def put(parcel_id):
		order = ParcelModel().cancel_order(parcel_id)
		return jsonify({
			"Status": "Order cancelled",
			"Order" : order
		}), 201

	@parcel_v1.route('/<string:username>/parcels', methods=['GET'])
	def get_user(username):
		user = ParcelModel().user_orders_by_username(username)
		return jsonify({
			"Message": "Hurray! It worked!!!",
			"User" : user
		})





	





