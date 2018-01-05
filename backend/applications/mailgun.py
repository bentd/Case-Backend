#! ../../env/bin/python

import requests

from server import app


def sendEmail(to, subject, template):

    domain = app.config["MAILGUN_DOMAIN"]
    sender = app.config["MAILGUN_DEFAULT_SENDER"]
    key = app.config["MAILGUN_API_KEY"]

    url = "https://api.mailgun.net/v3/{domain}/messages".format(domain=domain)
    auth = ("api", key)
    data = {"from": sender , "to": [to], "subject": subject, "html": template}

    return requests.post(url, auth=auth, data=data)
