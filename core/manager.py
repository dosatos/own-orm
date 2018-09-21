import re
import sqlite3



__version__ = 'ORM Version 0.1'


def create_engine(db_name):
    conn = sqlite3.connect(db_name)
    return conn