from flask import Flask, Blueprint
from .api.v1.views.user_views import parcel_v1 as v1
#from db_config import create_tables, destroy_tables

def parcel_app():
	app = Flask(__name__)
	#destroy_tables()
	#create_tables()

	#Register the blueprint you want to use/run
	app.register_blueprint(v1, url_prefix='/api/v1/parcels')

	return app

