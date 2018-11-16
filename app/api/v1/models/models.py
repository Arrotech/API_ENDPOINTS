parcels = []

class ParcelModel():         

	def __init__(self):
		self.orders = parcels

	def save(self, sender_name, recipient, destination, pickup, weight, username):
		delivery_order = {
		"parcel_id" : len(self.orders)+1,
		"senderName" : sender_name,
		"recipient" : recipient,
		"destination" : destination,
		"pickup" : pickup,
		"weight" : weight,
		"username" : username,
		"Status" : "In-Transit"
		
		}
		self.orders.append(delivery_order)
		return self.orders

	def get_all_parcels(self):
		return self.orders

	def get_parcel_by_id(self, parcel_id):
		if self.orders:
			for order in self.orders:
				if order.get('parcel_id') == parcel_id:
					return order

	def cancel_order(self, parcel_id):
		for parcel in self.orders:
			if parcel_id == parcel['parcel_id']:
				parcel.update({"status" : "Cancelled"})

	def delete_order(self, parcel_id):
		for order in self.orders:
			if parcel_id == order['parcel_id']:
				order.update({"status" : "Deleted"})

	def user_orders_by_username(self, username):
		users = [
		{
		"sender_name": "Harun",
		"recipient": "Peter",
		"destination": "Nakuru",
		"pickup": "Nairobi",
		"weight": "25kg",
		"username": "ogol"
		},
		{
		"sender_name": "Jane",
		"recipient": "Samuel",
		"destination": "kisii",
		"pickup": "eldoret",
		"weight": "13kg",
		"username": "mercy"
		},
		{
		"sender_name": "Kane",
		"recipient": "Marta",
		"destination": "machakos",
		"pickup": "kisumu",
		"weight": "7kg",
		"username": "arrotech"
		}
		]
		if users:
			for user in users:
				if user.get('username') == username:
					return user, 200






