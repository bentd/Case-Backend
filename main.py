#! /usr/bin/python


from flask import Flask
from flask import make_response
from flask import redirect
from flask import Response
from flask import request
from flask import url_for
from jinja2 import Environment
from jinja2 import FileSystemLoader
from flask import Flask
from flask.json import loads
from flask_cors import CORS, cross_origin

from query import *


engine = create_engine("mysql+pymysql://root:8?At7NYQeDa7tjU#TD%Uv6r5CTHe5Y-4@35.196.32.114:3306/casedb") # append to end of file
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


app = Flask(__name__)


@app.route("/")
def main():

    return "Hello World"

@app.route("/adduser/", methods=["POST", "OPTIONS"])
@cross_origin()
def adduser():

    data = loads(request.data)

    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    first = data.get("first")
    last = data.get("last")
    verify = data.get("verify")

    print username, password, email, last, verify

    user = User(email=email, first=first, last=last, phash=password)
    session.add(user)
    session.commit()

    return ""


if __name__ == "__main__":

    app.run(host="127.0.0.1", port=8080, debug=True)
