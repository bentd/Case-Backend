#! env/bin/python

import os
import unittest
import coverage
import datetime
import subprocess

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

"""
COV = coverage.coverage(
        branch=True,
        include='project/*',
        omit=['*/__init__.py', '*/config/*']
    )
COV.start()
"""

from server import app, db


migrate = Migrate(app, db)
manager = Manager(app)

# migrations
manager.add_command('db', MigrateCommand)


@manager.command
def createdb():
    """Creates the db tables."""

    db.create_all()

@manager.command
def dropdb():
    """Drops the db tables."""

    db.drop_all()

@manager.command
def test():

    tests = unittest.TestLoader().discover('tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    return 0 if result.wasSuccessful() else 1

@manager.command
def coverage():

    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    COV.stop()
    COV.save()
    print('Coverage Summary:')
    COV.report()
    basedir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'tmp/coverage')
    COV.html_report(directory=covdir)
    print('HTML version: file://%s/index.html' % covdir)
    COV.erase()

@manager.command
def start(config):

    configs = {"dev": "server.config.DevelopmentConfig",
               "test": "server.config.TestingConfig",
               "prod": "server.config.ProductionConfig"}
    app.config.from_object(configs[config])
    db.create_all()
    app.run(host="0.0.0.0", port=80, debug=True)


if __name__ == '__main__':

    manager.run()
