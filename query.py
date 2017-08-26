#! /usr/bin/python


import sys

import pymysql

from sqlalchemy import Column, ForeignKey, Integer, String, Text, BIGINT

from sqlalchemy.dialects import mysql

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class User(Base):

    __tablename__ = "users"

    id = Column(mysql.BIGINT, primary_key=True)

    email = Column(Text)

    first = Column(Text)

    last = Column(Text)

    phash = Column(Text)

    pic = Column(Text)



engine = create_engine("mysql+pymysql://root:8?At7NYQeDa7tjU#TD%Uv6r5CTHe5Y-4@35.196.32.114:3306/casedb") # append to end of file
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session = DBSession()

# user = User(email="dylan1.bent@famu.edu", first="Dylan", last="Wilkins", phash="93e890jelj")

#session.add(user)
# session.commit()
