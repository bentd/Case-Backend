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

class Post(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    imageurl = db.Column(db.String(128))
    condition = db.Column(db.String(16), nullable=False)
    description = db.Column(db.String(140), nullable=False)
    price = db.Column(db.Float(2), nullable=False)
    userid = db.Column(db.Integer, db.ForeignKey("users.id"))
    schoolid = db.Column(db.Integer, db.ForeignKey("schools.id"))

    user = db.relationship("User")
    school = db.relationship("School")

    def __init__ (self,
                  title,
                  condition,
                  description,
                  price,
                  userid,
                  schoolid,
                  imageurl=None):

        self.title = title
        self.imageurl = imageurl
        self.condition = condition
        self.description = description
        self.price = price
        self.userid = userid
        self.schoolid = schoolid

    def add(self):

        db.session.add(self)
        db.session.commit()

    @property
    def serialize(self):

        return {"title": self.title,
                "image": self.image_url,
                "condition": self.condition,
                "description": self.description,
                "price": self.price,
                "user": self.user.firstName,
                "email": self.user.email}

    @staticmethod
    def fromForm(form):

        title = form.title.data
        imageurl = form.imageurl.data
        condition = form.condition.data
        description = form.description.data
        price = form.price.data
        userid = form.userid.data
        schoolid = form.schoolid.data
        return Post(title, condition, description, price, userid, schoolid, imageurl=imageurl)
