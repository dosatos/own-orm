import re
import sqlite3



__version__ = 'ORM Version 0.1'


def create_engine(db_name):
    conn = sqlite3.connect(db_name)
    return conn


class Session:
    def __init__(self, bind=None):
        self.engine = bind

    def configure(self, bind=None):
        self.engine = bind

    def create_table(self, instance):
        query = f"CREATE TABLE IF NOT EXISTS {instance.__tablename__} ({', '.join(instance.fields)})"
        c = self.engine.cursor()
        c.execute(query)

    def add(self, instance):
        c = self.engine.cursor()
        qmark = '?'
        params = f"{', '.join([qmark for _ in range(len(instance.fields))])}"
        c.execute(f'INSERT INTO {instance.__tablename__} VALUES ({params})', instance.fields)


    def save(self):
        self.engine.commit()
        self.engine.close()