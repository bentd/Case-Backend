#! env/bin/python

import os
import unittest
import coverage
import datetime
import subprocess

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


COV = coverage.coverage(branch=True,
                        include="project/*",
                        omit=["*/__init__.py", "*/config/*"])
COV.start()


from server import app, db

migrate = Migrate(app, db)
manager = Manager(app)

# migrations
manager.add_command('db', MigrateCommand)
"""
1) python manage.py db init
2) python manage.py db migrate
3) python manage.py db upgrade
"""


@manager.command
def createdb():
    """Creates the db tables."""

    db.create_all()

@manager.command
def addschools():
    """Adds schools to database."""

    # adds schools to database
    wdir = os.getcwd()
    with open("/Users/bentd/OneDrive/Business/Startup/Case/Code/Backend/server/database/schools.json", "r") as schools:

        schools = schools.read() # read from json file
        schools = json.loads(schools) # convert json to python dictionary
        schools = schools["schools"] # get the dictionary from schools keys
        abbrs = schools.keys() # get school abbreviations
        abbrs.sort() # sort school Names

        for abbr in abbrs:

            name = schools[abbr]

            if len(abbr) > 8 or abbr == None:
                db.session.add(School(name=name))
            else:
                db.session.add(School(name=name, abbr=abbr))
            db.session.commit()

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


if __name__ == '__main__':

    manager.run()
