from flask import Flask, Blueprint
from .api.v1.views.user_views import parcel_v1 as v1

def parcel_app():
	app = Flask(__name__)
	app.register_blueprint(v1, url_prefix='/api/v1/')
	return app

