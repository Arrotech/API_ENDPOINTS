import unittest
from app import parcel_app
import json
from app.api.v1.views import user_views
from app.api.v1.models.models import ParcelModel
from flask import request


class TestDataParcel(unittest.TestCase):

    def setUp(self):
        self.app = parcel_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        self.data = {
        "sender_name": "Harun",
        "recipient": "Peter",
        "destination": "Nakuru",
        "pickup": "Nairobi",
        "weight": "25kg",
        "username": "arrotech"
        }

    def test_post(self):
        response = self.client.post(
            '/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)

    def test_get(self):
        response = self.client.get(
            '/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_get_parcel_by_id(self):
        response = self.client.get(
            '/api/v1/parcels/1', data=json.dumps(self.data), content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_cancel_unexisting_order(self):
        response = self.client.put('/api/v1/parcels/1/cancel',data=json.dumps(self.data), content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result["Message"], "Unavailable order")
        assert response.status_code == 200

    def test_get_user(self):
        response = self.client.get(
            '/api/v1/user/arrotech/parcels', data=json.dumps(self.data), content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_get_unexisting_user(self):
        user = []
        response = self.client.get(
            '/api/v1/user/arrotech/parcels', data=json.dumps(user), content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

    '''def test_delete_existing_order(self):
        response = self.client.delete('/api/v1/parcels/<int:parcel_id>/delete', data=json.dumps(self.data), content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_delete_unexisting_order(self):
        data = {}
        response = self.client.delete('/api/v1/parcels/<int:parcel_id>/delete', data=json.dumps(data), content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result["Message"], "Order Unavailable", msg="Not allowed")
        assert response.status_code == 400'''

    def test_incorrect_post_url(self):
        response=self.client.post()
        self.assertEqual(response.status, '404 NOT FOUND')

    def test_invalid_get_product_url(self):
        response=self.client.get()
        self.assertEqual(response.status, '404 NOT FOUND')


    '''def test_username_is_empty(self):
        incorrect = {
            "sender_name": "Harun",
            "recipient": "Peter",
            "destination": "Nakuru",
            "pickup": "Nairobi",
            "weight": "25kg",
            "username": ""
        }
        response = self.client.post(
            '/api/v1/parcels', data=json.dumps(incorrect), content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result['Message'],
           "Hurray! It worked!!!", msg="Username cannot be empty")

    def test_empty_key(self):
        incorrect = {
            "sender_name": "Harun",
            "": "Peter",
            "destination": "Nakuru",
            "pickup": "Nairobi",
            "weight": "25kg",
            "username": "john"
        }
        response = self.client.post(
            '/api/v1/parcels', data=json.dumps(incorrect), content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result['Message'],
           "Hurray! It worked!!!", msg="Username cannot be empty")

    def test_empty_values(self):
        incorrect = {
            "sender_name": "Harun",
            "recipient": "Peter",
            "destination": "",
            "pickup": "Nairobi",
            "weight": "25kg",
            "username": ""
        }
        response = self.client.post(
            '/api/v1/parcels', data=json.dumps(incorrect), content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result['Message'],
           "Hurray! It worked!!!", msg="Username cannot be empty")
    
    def test_invalid_data_types(self):
        
        response=self.check_invalid_data_type()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['Error'],"Require int or float type")
        self.assertEqual(response.status_code, 200)

    def test_get_missing_orders(self):
        
        response=self.get_unexisting_products()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['message'],"No Available products")
        self.assertEqual(response.status_code, 200)

    def test_create_new_order(self):
       
        response=self.add_new_product()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201, result['New Product'])'''

    

    



if __name__ == "__main__":
    unittest.main()
