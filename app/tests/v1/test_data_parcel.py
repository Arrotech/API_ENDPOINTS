import unittest
from ...app import parcel_app
import os
import tempfile

class TestDataParcel(unittest.TestCase):
	def setUp():
		parcel_app().app.testing = True
		self.app = parcel_app().app.test_client()

		self.details = {
			"ParcelId": len(ParcelModel.parcels)+1,
	        "sender_name" : "Harun",
	        "recipient": "Peter",
	        "destination": "Nakuru",
	        "pickup": "Nairobi" ,
	        "weight" : "25kg"
		}

	def test_post(self):
		response = self.app.post('/api/v1/parcels',data=json.dumbs(), content_type='json')
		result = json.loads(response.data)
		self.assertEqual(response.status_code,201)

	def test_get(self):
		response = self.app.get('/api/v1/parcels',data=json.loads(), content_type='json')
		result = json.loads(response.data)
		self.assertEqual(response.status_code,201)

if __name__ == "__main__":
	app.run(debug=True)



