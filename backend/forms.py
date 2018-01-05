#! ../../env/bin/python

import re

from server import db
from server.database.users import User
from wtforms import FloatField
from wtforms import Form
from wtforms import IntegerField
from wtforms import PasswordField
from wtforms import StringField
from wtforms import TextField
from wtforms.validators import DataRequired as Required
from wtforms.validators import Length
from wtforms.validators import EqualTo


def ValidEmail(form, email):

    regex = r"(^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    print re.match(regex, email.data)
    if re.match(regex, email.data):
        return True
    email.errors.append("Invalid email")
    return False

def UniqueEmail(form, email):

    if User.exists(email.data):
        email.errors.append("Email already exists")
        return False
    return True


def RegisteredEmail(form, email):

    return User.exists(email.data)


class SignupForm(Form):

    fname = StringField("First Name", [Required(), Length(max=32)])
    lname = StringField("Last Name", [Required(), Length(max=32)])
    email = TextField("Email", [Required(), ValidEmail, UniqueEmail, Length(min=6, max=64)])
    password = PasswordField("Password", [Required(), Length(min=6, max=256)])
    confirm = PasswordField("Repeat Password", [Required(), Length(min=6, max=256), EqualTo("password", message="Passwords must match")])


class LoginForm(Form):

    email = TextField("Email", [Required(), ValidEmail, Length(min=6, max=64), RegisteredEmail])
    password = PasswordField("Password", [Required(), Length(min=6, max=256)])


class ForgotPasswordForm(Form):

    email = TextField("Email", [Required(), ValidEmail, Length(min=6, max=256), RegisteredEmail])


class ChangePasswordForm(Form):

    old = PasswordField("Old Password", [Required(), Length(min=6, max=256)])
    password = PasswordField("Password", [Required(), Length(min=6, max=256)])
    confirm = PasswordField("Repeat Password", [Required(), Length(min=6, max=256), EqualTo("Password", message="Passwords must match")])


class PostForm(Form):

    title = StringField("Title", [Required(), Length(max=40)])
    imageurl = StringField("Image URL")
    condition = StringField("Condition", [Required(), Length(max=16)])
    description = StringField("Description", [Required(), Length(max=140)])
    price = FloatField("Price", [Required()])
    userid = IntegerField("User ID", [Required()])
    schoolid = IntegerField("School ID", [Required()])
