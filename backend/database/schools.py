#! ../../env/bin/python

import datetime
import json
import random
import string

from itsdangerous import BadSignature
from itsdangerous import SignatureExpired
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from server import app
from server import bcrypt
from server import db


class School(db.Model):

    __tablename__ = "schools"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    abbr = db.Column(db.String(16), nullable=True)

    def __init__(self,
                 name,
                 abbr=None):

        self.name = name
        self.abbr = abbr

    @property
    def serialize(self):

        return {"id": self.id,
                "name": self.name,
                "abbr": self.abbr}
