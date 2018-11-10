'''from app.api.v1.views.user_views import DataParcel
from flask import Blueprint
from flask_restful import Api, Resource


parcel_v1 = Blueprint('v1', __name__,url_prefix='/api/v1/')
api = Api(parcel_v1)

api.add_resource(DataParcel, '/parcels')
#api.add_resource(SingleParcel, '/parcels/<int:id>')'''
