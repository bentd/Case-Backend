#! ../../env/bin/python

from flask import Blueprint
from flask import request
from flask import Response
from server import auth


posts = Blueprint("posts", __name__)


@posts.route("/posts", methods=["POST"])
@auth.login_required
def createPost():

    return Response(str(request.json), status=400)


@posts.route("/posts/<int:id>", methods=["GET"])
@auth.login_required
def retrievePost(id):

    return Response(str(request.json) + str(id), status=400)


@posts.route("/posts/<int:id>", methods=["PUT"])
@auth.login_required
def updatePost(id):

    return Response(str(request.json) + str(id), status=400)


@posts.route("/posts/<int:id>", methods=["DELETE"])
@auth.login_required
def deletePost(id):

    return Response(str(request.json) + str(id), status=400)


@posts.route("/posts", methods=["GET"])
@auth.login_required
def retrievePosts():

    return Response(str(request.json), status=400)
