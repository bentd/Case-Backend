#! ../env/bin/python

import os

from flask import Flask
from flask import g
from flask import Response
from flask_bcrypt import Bcrypt
from flask_httpauth import HTTPBasicAuth
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ.get("APP_SETTINGS", "server.config.DevelopmentConfig"))


bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
mail = Mail(app)


# from server.database.posts import Post
# from server.database.schools import School
from server.database.users import User
db.create_all()


auth = HTTPBasicAuth()
@auth.verify_password
def verify(identifier, password):

    user = User.verifyUser(identifier, password)
    if user:
        g.user = user
        return True
    return False

from server.routes.accounts import accounts
from server.routes.posts import posts
from server.routes.schools import schools
from server.routes.tokens import tokens

app.register_blueprint(accounts)
app.register_blueprint(posts)
app.register_blueprint(schools)
app.register_blueprint(tokens)



@app.errorhandler(403)
def forbidden(error):
    return Response(error, status=403)


@app.errorhandler(404)
def lost(error):
    return Response(error, status=404)


@app.errorhandler(500)
def error(error):
    return Response(error, status=500)


if __name__ == "__main__":

    app.run(host="127.0.0.1", port=80, debug=True)
