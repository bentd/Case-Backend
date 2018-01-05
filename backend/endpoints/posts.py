#! ../../env/bin/python

from flask import Blueprint
from flask import jsonify
from flask import request
from flask import Response
from server import auth
from server import db
from server.database.posts import Post
from server.forms import PostForm


posts = Blueprint("posts", __name__)


@posts.route("/post", methods=["POST"])
@auth.login_required
def createPost():

    form = PostForm(data=request.json)
    if form.validate():
        # add post
        post = Post.fromForm(form)
        post.add()
        return jsonify(post.serialize), 200
    return jsonify(form.errors), 400


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

    school_id = request.args.get("school_id")
    offset = request.args.get("offset", 0)
    posts = db.session.query(Post).filter_by(school_id=school_id).limit(10).offset(offset).all()
    posts = [post.serialize for post in posts]
    return jsonify(posts), 200
