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
                  user_id,
                  school_id,
                  image_url=None):

        self.title = title
        self.image_url = image_url
        self.condition = condition
        self.description = description
        self.price = price
        self.user_id = user_id
        self.school_id = school_id

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
        image_url = form.image_url.data
        condition = form.condition.data
        description = form.description.data
        price = form.price.data
        user_id = form.user_id.data
        school_id = form.school_id.data
        return Post(title, condition, description, price, user_id, school_id, image_url=image_url)
