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
        # add user to database
        user = User.fromForm(form)
        db.session.add(user)
        db.session.commit()
        # send confirmation email
        token = user.generateToken(expiry=172800)
        url = url_for("accounts.confirm", token=token, _external=True)
        template = render_template("confirm/email.html", url=url)
        sendEmail(user.email, "Confirm Case App Account", template)
        # return user information
        json = user.serialize
        json.update({"token": user.generateToken()})
        return jsonify(json)
    # return errors if any
    return jsonify(form.errors), 400


@accounts.route("/account/confirm", methods=["POST"])
@auth.login_required
def sendConfirmation():

    token = g.user.generateToken()
    url = url_for("accounts.confirm", token=token, _external=True)
    template = render_template("confirm/email.html", url=url)
    sendEmail(g.user.email, "Confirm Case App Account", template)
    return "Confirmation sent", 200


@accounts.route("/account/confirm/<string:token>", methods=["GET"])
def confirm(token):

    user = User.verifyUser(token)
    if user:
        if not user.confirmed:
            user.confirmed = datetime.datetime.utcnow()
            db.session.add(user)
            db.session.commit()
        return redirect(url_for("accounts.confirmed", token=token))
    return "User not found", 404


@accounts.route("/account/confirmed/<string:token>", methods=["GET"])
def confirmed(token):

    user = User.verifyUser(token)
    if user:
        return render_template("confirm/confirmed.html", user=user)
    abort(500)


@accounts.route("/account", methods=["GET"])
@auth.login_required
def login():

    json = g.user.serialize
    json.update({"token": g.user.generateToken()})
    return jsonify(json)


@accounts.route("/account", methods=["PUT"])
@auth.login_required
def updateAccount():

    form = EditAccountForm(data=request.json)
    if form.validate:
        return "", 200
    return "", 400


@accounts.route("/account", methods=["DELETE"])
@auth.login_required
def deleteAccount():

    return Response(str(request.json), status=200)
