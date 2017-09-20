#! ../../env/bin/python

from flask import Blueprint
from flask import jsonify
from flask import request
from flask import Response
from server import auth
from server import db
from server.database.schools import School


schools = Blueprint("schools", __name__)


@schools.route("/schools", methods=["GET"])
def retrieveSchools():

    schools = [school.serialize for school in db.session.query(School).all()]
    return jsonify(schools)
