#! ../../env/bin/python

import datetime
import random
import string

from itsdangerous import BadSignature
from itsdangerous import SignatureExpired
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from random import choice
from server import app
from server import bcrypt
from server import db
from string import digits


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, nullable=False)
    phash = db.Column(db.String(64), nullable=False)
    fname = db.Column(db.String(64), nullable=False)
    lname = db.Column(db.String(64), nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    confirmed = db.Column(db.DateTime, nullable=True)
    vcode = db.Column(db.String(6), nullable=True)

    def __init__(self,
                 email,
                 password,
                 fname,
                 lname):

        self.email = email
        self.phash = self.hashPassword(password)
        self.fname = fname
        self.lname = lname
        self.created = datetime.datetime.utcnow()
        self.confirmed = None
        self.vcode = self.generateCode()

    def hashPassword(self, password):

        return bcrypt.generate_password_hash(password)

    def verifyPassword(self, password):

        return bcrypt.check_password_hash(self.phash, password)

    def generateCode(self):

        return "".join(choice(digits) for i in range(6))

    def generateToken(self, expiry=None):

        return User.Serializer(expiry).dumps({"email": self.email})

    def add(self):

        db.session.add(self)
        db.session.commit()

    def update(self, form):

        self.phash =  self.phash if (self.verifyPassword(form.password.data)) else self.hashPassword(password)
        self.confirmed = None if (self.email != form.email.data) else self.confirmed
        self.email = form.email.data
        self.fname = form.fname.data
        self.lname = form.lname.data

    def delete(self):

        db.session.delete(self)
        db.session.commit()

    @property
    def serialize(self):

        return {"email": self.email,
                "fname": self.fname,
                "lname": self.lname,
                "confirmed": self.confirmed}

    @staticmethod
    def fromForm(form):

        email = form.email.data
        password = form.password.data
        fname = form.fname.data
        lname = form.lname.data
        return User(email=email, password=password, fname=fname, lname=lname)

    @staticmethod
    def exists(email):

        user = db.session.query(User).filter_by(email=email).first()
        return True if user else False

    @staticmethod
    def Serializer(expiry=None):

        key = app.config["SECRET_KEY"]
        salt = app.config['SECURITY_PASSWORD_SALT']
        return Serializer(key, salt=salt, expires_in=expiry)

    @staticmethod
    def verifyToken(token, expiry=None):

        try:
            return User.Serializer(expiry).loads(token).get("email")
        except SignatureExpired:
            return None
        except BadSignature:
            return None

    @staticmethod
    def verifyUser(email_or_token, password=None, expiry=None):

        emailFromToken = User.verifyToken(email_or_token, expiry)
        if emailFromToken:
            return db.session.query(User).filter_by(email=emailFromToken).first()
        else:
            user = db.session.query(User).filter_by(email=email_or_token).first()
            return None if (not user or not user.verifyPassword(password)) else user
