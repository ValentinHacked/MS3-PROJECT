from flask import Flask

from .extensions import mongo


def create_app_():
    app = Flask(__name__)

    app.config['MONGO_URI'] = 'mongodb+srv://ValentinVM:<Password1>@cluster0.qc3we.mongodb.net/mydb?retryWrites=true&w=majority'

    mongo.init_app(app)

    return app
