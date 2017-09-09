#! ../../env/bin/python

import datetime
import random
import string

from itsdangerous import BadSignature
from itsdangerous import SignatureExpired
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from server import app
from server import bcrypt
from server import db


class User(db.Model):

    __tablename__ = "users"

    uid = db.Column(db.Integer, primary_key=True) #autoincrement="auto")
    email = db.Column(db.String(64), unique=True, nullable=False)
    phash = db.Column(db.String(64), nullable=False)
    firstName = db.Column(db.String(64), nullable=False)
    lastName = db.Column(db.String(64), nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    confirmed = db.Column(db.DateTime, nullable=True)
    reset = db.Column(db.String(64), nullable=True)

    def __init__(self,
                 email,
                 password,
                 firstName,
                 lastName,
                 confirmed=None,
                 reset=None):

        self.email = email
        self.phash = self.hashPassword(password)
        self.firstName = firstName
        self.lastName = lastName
        self.created = datetime.datetime.utcnow()
        self.confirmed = confirmed
        self.reset = reset

    def generateToken(self, expiry=None):

        return User.Serializer(expiry).dumps({"email": self.email})

    def hashPassword(self, password):

        return bcrypt.generate_password_hash(password)

    def verifyPassword(self, password):

        return bcrypt.check_password_hash(self.phash, password)

    def update(self, form):

        self.phash =  self.phash if (self.verifyPassword(form.password.data)) else self.hashPassword(password)
        self.confirmed = None if (self.email != form.email.data) else self.confirmed
        self.email = form.email.data
        self.firstName = form.firstName.data
        self.lastName = form.lastName.data

    @classmethod
    def fromForm(cls, form):

        email = form.email.data
        password = form.password.data
        firstName = form.firstName.data
        lastName = form.lastName.data
        return User(email=email, password=password, firstName=firstName, lastName=lastName)

    @property
    def serialize(self):

        return {"email": self.email,
                "firstName": self.firstName,
                "lastName": self.lastName,
                "confirmed": self.confirmed}

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
