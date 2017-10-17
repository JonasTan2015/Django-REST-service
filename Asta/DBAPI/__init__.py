'''
MySQL-python does not support python3
mysqlclient is no longer supported

To use pymysql, paste these lines in the init file
'''

import pymysql
pymysql.install_as_MySQLdb()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:12345@localhost/asta")
Session = sessionmaker(bind=engine)