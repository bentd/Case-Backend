
import pymysql

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:8?At7NYQeDa7tjU#TD%Uv6r5CTHe5Y-4@35.196.32.114:3306/casedb")

Base = declarative_base()
Base.metadata.bind = engine

Session = sessionmaker(bind=engine)
session = DBSession()
