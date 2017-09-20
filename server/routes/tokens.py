#! ../../env/bin/python

from flask import Blueprint
from flask import g
from flask import request
from flask import Response
from server import auth


tokens = Blueprint("tokens", __name__)


@tokens.route("/tokens", methods=["POST"])
@auth.login_required
def createToken():

    return g.user.generateToken()


@tokens.route("/tokens", methods=["GET"])
@auth.login_required
def retrieveToken(id):

    return Response(str(id), status=400)


@tokens.route("/tokens", methods=["PUT"])
@auth.login_required
def updateToken(id):

    return Response(str(request.json) + str(id), status=400)


@tokens.route("/tokens", methods=["DELETE"])
@auth.login_required
def deleteToken(id):

    return Response(str(request.json) + str(id), status=400)
