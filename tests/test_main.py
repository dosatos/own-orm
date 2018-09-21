import os
import glob
import pytest

from orm.core import manager
from orm.core import models


class User(models.Model):
    __tablename__ = "user"

    name = models.CharField()
    email = models.EmailField()



class BadUser(models.Model):
    name = models.CharField()
    email = models.EmailField()



class TestModel():

    @pytest.mark.parametrize("name, email, result", [
        ("yeldos", "hello@wrold.com", ['name', 'email']),

    ])
    def test_char_and_email_field_success(self, name, email, result):
        user = User(name=name, email=email)
        assert user.fields == result and user.name == name and user.email == email

    def test_tablename_setup_success(self):
        name, email = 'yeldos', 'yeldos@gmail.com'
        user = User(name=name, email=email)

    def test_tablename_is_missing(self):
        name, email = 'yeldos', 'yeldos@gmail.com'
        with pytest.raises(AttributeError):
            user = BadUser(name=name, email=email)



class TestORM:

    @pytest.fixture
    def engine(self):
        db_name = 'sqlite.db'
        return manager.create_engine(db_name)

    def test_engine_created_success(self):
        db_name = 'sqlite.db'
        manager.create_engine(db_name)
        assert db_name in glob.glob('*')
    #
    # def test_create_table_in_db(self, engine):
    #     pass
    #
    # def test_query_db(self):
    #     pass
    #
    # def test_create_table_success(self, engine):
    #     session = manager.Session(bind=engine)
    #     session.add(User())
    #     session.query(User())
