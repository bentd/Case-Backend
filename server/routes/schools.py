#! ../../env/bin/python

from flask import Blueprint
from flask import request
from flask import Response
from server import auth


schools = Blueprint("schools", __name__)


@schools.route("/schools", methods=["POST"])
@auth.login_required
def createPost():

    return Response(request.json, status=400)


@schools.route("/schools/<int:id>", methods=["GET"])
@auth.login_required
def retrievePost(id):

    return Response(str(request.json) + str(id), status=400)


@schools.route("/schools/<int:id>", methods=["PUT"])
@auth.login_required
def updatePost(id):

    return Response(str(request.json) + str(id), status=400)


@schools.route("/schools/<int:id>", methods=["DELETE"])
@auth.login_required
def deletePost(id):

    return Response(str(request.json) + str(id), status=400)


@schools.route("/schools", methods=["GET"])
@auth.login_required
def retreiveSchools():

    return Response(str(request.json), status=400)
