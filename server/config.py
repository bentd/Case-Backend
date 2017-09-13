# ../env/bin/python

import os

serverdir = os.path.abspath(os.path.dirname(__file__))
databasedir = os.path.abspath(os.path.join(serverdir, "database"))

class BaseConfig(object):
    """Base configuration."""

    # main config
    BCRYPT_LOG_ROUNDS = 13
    DEBUG = False
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SECRET_KEY = "$3CR3+"
    SECURITY_PASSWORD_SALT = ""
    WTF_CSRF_ENABLED = True

    # mail settings
    MAIL_PORT = 587
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    # mail authentication and sender
    MAIL_USERNAME = "code@dylanbent.com"
    MAIL_PASSWORD = "dcwvbpbayrmcotuy"
    MAIL_DEFAULT_SENDER = "code@dylanbent.com"

    #database
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #location
    LOCATION = "http://localhost"


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    # main config
    DEBUG = True
    DEBUG_TB_ENABLED = True
    WTF_CSRF_ENABLED = False

    # database URI
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(databasedir, "dev.sqlite")


class TestingConfig(BaseConfig):
    """Testing configuration."""

    # main config
    BCRYPT_LOG_ROUNDS = 1
    TESTING = True
    WTF_CSRF_ENABLED = False

    # database URI
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:8?At7NYQeDa7tjU#TD%Uv6r5CTHe5Y-4@35.196.58.16:3306/casedb"

    #location
    LOCATION = "http://case-app-backend.appspot.com"


class ProductionConfig(BaseConfig):
    """Production configuration."""

    # main config
    SECRET_KEY = "SECRET_KEY"
    SECURITY_PASSWORD_SALT = "SECRET_KEY"

    # database URI

    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "mysql+pymysql://root:8?At7NYQeDa7tjU#TD%Uv6r5CTHe5Y-4@/casedb?unix_socket=/cloudsql/case-app-backend:us-east1:casedb")

    #location
    LOCATION = "http://case-app-backend.appspot.com"

    # stripe keys
    STRIPE_SECRET_KEY = "STRIPE_SECRET_KEY"
    STRIPE_PUBLISHABLE_KEY = "STRIPE_PUBLISHABLE_KEY"
