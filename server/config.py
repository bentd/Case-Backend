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

    # mailgun config
    # MAILGUN_DOMAIN = "sandbox6868f737eeb34d2eb7efa45ab1ad7ed4.mailgun.org"
    # MAILGUN_DEFAULT_SENDER = "Case Team <mailgun@sandbox6868f737eeb34d2eb7efa45ab1ad7ed4.mailgun.org>"
    # MAILGUN_API_KEY = "key-e24110eb9c03ec59ff02fd222893ee3b"

    MAILGUN_DOMAIN = "mg.caseapp.co"
    MAILGUN_DEFAULT_SENDER = "Case Team <support@caseapp.co>"
    MAILGUN_API_KEY = "key-e24110eb9c03ec59ff02fd222893ee3b"

class ProductionConfig(BaseConfig):
    """Production configuration."""

    # database URI
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")

    # stripe keys
    STRIPE_SECRET_KEY = "STRIPE_SECRET_KEY"
    STRIPE_PUBLISHABLE_KEY = "STRIPE_PUBLISHABLE_KEY"
