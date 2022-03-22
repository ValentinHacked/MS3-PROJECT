from flask import Flask

from .extensions import mongo

def create_app_():
    app = Flask(__name__)

    mongo.init_app(app)

    return app