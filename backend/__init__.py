#! /env/bin/python

import os

from flask import Flask
from flask import g
from flask import Response
from flask import request
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy


assert os.environ.get("APP_SETTINGS"), "App Isn't Configured!"

app = Flask(__name__)
app.config.from_object(os.environ.get("APP_SETTINGS"))
CORS(app)


bcrypt = Bcrypt(app)
db = SQLAlchemy(app)


from server.database.posts import Post
from server.database.schools import School
from server.database.users import User


auth = HTTPBasicAuth()
@auth.verify_password
def verify(identifier, password):

    user = User.verifyUser(identifier, password)
    if user:
        g.user = user
        return True
    return False


from backend.endpoints.accounts import accounts
from backend.endpoints.posts import posts
from backend.endpoints.schools import schools
from backend.endpoints.tokens import tokens

app.register_blueprint(accounts)
app.register_blueprint(posts)
app.register_blueprint(schools)
app.register_blueprint(tokens)


@app.before_request
def before():

    if "paas-url" in request.url:
        abort(400)


@app.errorhandler(403)
def forbidden(error):
    return Response(error, status=403)


@app.errorhandler(404)
def lost(error):
    return Response(error, status=404)


@app.errorhandler(500)
def error(error):
    return Response(error, status=500)
