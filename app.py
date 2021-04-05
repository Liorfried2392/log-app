import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.log import Log, LogsList

app = Flask(__name__)

app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dtuslpttrvdgck:8061616320cdebba6157862b3ee490506ac39f05f75491115cca3f84beaa1c0d@ec2-54-73-68-39.eu-west-1.compute.amazonaws.com:5432/d6jfkoshrj9dkl'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'lior'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth
api.add_resource(Log, '/log')
api.add_resource(LogsList, '/logs')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()
    app.run(port=5000)
