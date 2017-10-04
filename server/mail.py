#! ../../env/bin/python

from flask_mail import Message
from server import app
from server import mail

def sendEmail(to, subject, template):

    msg = Message(subject,
                  recipients=[to],
                  html=template,
                  sender=app.config["MAIL_DEFAULT_SENDER"])
    with mail.connect() as conn:
        conn.send(msg)
    mail.send(msg)
