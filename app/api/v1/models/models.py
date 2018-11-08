parcels = []


class ParcelModel():

	def __init__(self):
		self.db = parcels

	def save(self, sender_name, recipient, destination, pickup, weight):
		payload = {
		"parcel_id" : len(self.db)+1,
		"senderName" : sender_name,
		"recipient" : recipient,
		"destination" : destination,
		"pickup" : pickup,
		"weight" : weight
		}
		self.db.append(payload)
		return self.db

	def get_all_parcels(self):
		return self.db

	

