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
    SECRET_KEY = "vNChtkUHtXrb7uRcvBfZhvXtcjLmjCfq"
    SECURITY_PASSWORD_SALT = "kbgmAEVt7n55BLJe"
    WTF_CSRF_ENABLED = True

    # mail settings
    MAIL_PORT = 587
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    # mail authentication and sender
    MAIL_USERNAME = "code@dylanbent.com"
    MAIL_PASSWORD = "gmfkxpyybwtkszab"
    MAIL_DEFAULT_SENDER = "code@dylanbent.com"

    #database
    SQLALCHEMY_TRACK_MODIFICATIONS = False


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
    BCRYPT_LOG_ROUNDS = 5
    DEBUG = True
    DEBUG_TB_ENABLED = True
    TESTING = True
    WTF_CSRF_ENABLED = False

    # database URI
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "mysql+pymysql://root:kmug07shTrnQYWNnjUwRMVEwsiQ2vZFD@35.196.58.16/casedb")


class ProductionConfig(BaseConfig):
    """Production configuration."""

    # database URI
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")

    # stripe keys
    STRIPE_SECRET_KEY = "STRIPE_SECRET_KEY"
    STRIPE_PUBLISHABLE_KEY = "STRIPE_PUBLISHABLE_KEY"
