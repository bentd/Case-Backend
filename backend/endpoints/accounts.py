#! ../../env/bin/python

import datetime
import json

from flask import abort
from flask import Blueprint
from flask import g
from flask import jsonify
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import Response
from flask import url_for
from server import auth
from server import db
from server.database.users import User
from server.forms import SignupForm
from server.mail import sendEmail


accounts = Blueprint("accounts", __name__)


@accounts.route("/account", methods=["POST"])
def signup():

    # check form for errors
    form = SignupForm(data=request.json)
    if form.validate():
        # create user from form
        # add user to database
        user = User.fromForm(form)
        user.add()
        # send confirmation email
        token = user.generateToken(expiry=172800)
        url = url_for("accounts.confirm", token=token, _external=True)
        template = render_template("confirm/email.html", code=user.vcode)
        print sendEmail(user.email, "Confirm Case App Account", template)
        # return user information
        json = user.serialize
        json.update({"token": user.generateToken()})
        return jsonify(json)
    # return errors if any
    return jsonify(form.errors), 400


@accounts.route("/account/confirm", methods=["POST"])
def confirm():

    return ""


@accounts.route("/account", methods=["GET"])
@auth.login_required
def login():

    data = g.user.serialize
    data.update({"token": g.user.generateToken()})
    return jsonify(data)


@accounts.route("/account", methods=["PUT"])
@auth.login_required
def updateAccount():

    form = EditAccountForm(data=request.json)
    if form.validate():
        g.user.update(form)
        db.session.add(user)
        db.session.commit()
        return "", 200
    return "", 400


@accounts.route("/account", methods=["DELETE"])
@auth.login_required
def deleteAccount():

    g.user.delete()
    return Response(str(request.json), status=200)
