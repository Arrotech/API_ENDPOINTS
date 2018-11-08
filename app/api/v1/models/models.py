parcels = []

class ParcelModel():

	def __init__(self):
		self.db = parcels

	def save(self, sender_name, recipient, destination, pickup, weight):
		payload = {
		"senderName" : sender_name,
		"recipient" : recipient,
		"destination" : destination,
		"pickup" : pickup,
		"weight" : weight
		}
		self.db.append(payload)

