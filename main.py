#! env/bin/python


import os

from flask import Flask
from flask import render_template
from flask import request
from flask import Response
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import Form
from wtforms.validators import DataRequired
from werkzeug import ImmutableMultiDict
from server import app
from server import db


if __name__ == "__main__":

    app.config.from_object(os.environ.get("APP_SETTINGS", "server.config.TestingConfig"))
    db.create_all()
    app.run(host="0.0.0.0", port=80)
