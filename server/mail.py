#! ../../env/bin/python

from flask_mail import Message
from server import app
from server import mail

def sendEmail(to, subject, template):

    with mail.connect() as conn:
        msg = Message(subject,
                      recipients=[to],
                      html=template,
                      sender=app.config["MAIL_DEFAULT_SENDER"])
        conn.send(msg)
