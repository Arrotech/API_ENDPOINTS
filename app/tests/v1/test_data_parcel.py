import unittest
from ... import parcel_app
import os
import tempfile
import json
from ...api.v1.views import user_views
from ...api.v1.models.models import ParcelModel




class TestDataParcel(unittest.TestCase):

    def setUp(self):
        self.app = parcel_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        self.data = {
        "parcel_id": "1",
        "sender_name": "Harun",
        "recipient": "Peter",
        "destination": "Nakuru",
        "pickup": "Nairobi",
        "weight": "25kg",
        "user_name": "arrotech",
        "Status" : "active"
        }

    def test_get(self):
        response = self.client.get(
            '/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result['Message'],
         "Hurray! It worked!!!", msg="Not allowed")
        assert response.status_code == 200

    def test_get_parcel_by_id(self):
        response = self.client.get(
            '/api/v1/parcels/1', data=json.dumps(self.data), content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result['Message'],
         "Hurray! It worked!!!", msg="Not allowed")
        assert response.status_code == 200

    def test_cancel_order(self):
      response = self.client.put('/api/v1/parcels/1/cancel',data=json.dumps(self.data), content_type='application/json')
      result = json.loads(response.data.decode())
      self.assertEqual(result['Status'], "Order cancelled", msg="Not allowed")
      assert response.status_code == 201



if __name__ == "__main__":
    unittest.main()
