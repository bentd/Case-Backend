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


@app.route("/email", methods=["GET"])
def email():

    url = "hello"
    temp = render_template("confirm/email.html", url=url)
    return temp, 200


if __name__ == "__main__":

    app.run(host="127.0.0.1", port=80, debug=True)
