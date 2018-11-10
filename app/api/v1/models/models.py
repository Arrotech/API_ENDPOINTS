parcels = []


class ParcelModel():         


	def __init__(self):
		self.db = parcels

	def save(self, sender_name, recipient, destination, pickup, weight, user_name):
		payload = {
		"parcel_id" : len(self.db)+1,
		"senderName" : sender_name,
		"recipient" : recipient,
		"destination" : destination,
		"pickup" : pickup,
		"weight" : weight,
		"user_name" : user_name
		}
		self.db.append(payload)
		return self.db

	def get_all_parcels(self):
		return self.db

	def get_parcel_by_id(self, parcel_id):
		if self.db:
			for order in self.db:
				if order.get('parcel_id') == parcel_id:
					return order
					
	def cancel_order(self, parcel_id):
		for parcel in self.db:
			if parcel_id == parcel['parcel_id']:
				parcel.update({"status" : "Cancelled"})

	def user_order(self, user_name):
		user_orders = []
		for user in self.db:
			if user_name == user['user_name']:
				user_orders.append(user)
		return user_orders
	

			




