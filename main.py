from flask import Flask
from flask import request, Response
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import Form
from wtforms.validators import DataRequired
from werkzeug import ImmutableMultiDict
from server import app


app.secret_key = "$3CR3+"


if __name__ == "__main__":

    app.run(host="127.0.0.1", port=80, debug=True)
