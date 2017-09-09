#! ../../env/bin/python

from server import db

from server.database.users import User
from wtforms import Form
from wtforms import PasswordField
from wtforms import StringField
from wtforms import TextField
from wtforms.validators import DataRequired as required
from wtforms.validators import Email
from wtforms.validators import Length
from wtforms.validators import EqualTo


class SignupForm(Form):


    firstName = StringField("First Name", [required(), Length(max=255)])
    lastName = StringField("Last Name", [required(), Length(max=255)])
    email = TextField("Email", [required(), Email(message="Invalid email"), Length(min=6, max=255)])
    password = PasswordField("Password", [required(), Length(min=6, max=255)])
    confirm = PasswordField("Repeat Password", [required(), EqualTo("password", message="Passwords must match")])

    def validate(self):

        initialValidation = super(SignupForm, self).validate()
        if not initialValidation:
            return False
        user = db.session.query(User).filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already exists")
            return False
        return True


class LoginForm(Form):

    email = TextField("Email", [required(), Email()])
    password = PasswordField("Password", [required()])


class ForgotPasswordForm(Form):

    email = TextField("Email", [required(), Email(), Length(min=6, max=255)])

    def validate(self):

        initial_validation = super(ForgotPasswordForm, self).validate()
        if not initial_validation:
            return False
        user = db.session.query(User).filter_by(email=self.email.data).first()
        if not user:
            self.email.errors.append("This email is not registered")
            return False
        return True


class ChangePasswordForm(Form):

    password = PasswordField("Password", [required(), Length(min=6, max=255)])
    confirm = PasswordField("Repeat password", [required(), EqualTo("Password", message="Passwords must match")])
