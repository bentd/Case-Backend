#! /usr/bin/python


import sys

import pymysql

from sqlalchemy import Column, ForeignKey, Integer, String, Text

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine


Base = declarative_base()


class Users(Base):

    __tablename__ = "users"

    id = Column(Serial, primary_key=True)

    email = Column(Text)

    first = Column(Text)

    last = Column(Text)

    phash = Column(Text)

    pic = Column(Text)



engine = create_engine("mysql+pymysql://root:8?At7NYQeDa7tjU#TD%Uv6r5CTHe5Y-4@35.196.32.114:3306/casedb") # append to end of file

Base.metadata.create_all(engine) # append to end of file
