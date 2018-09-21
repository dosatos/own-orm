import os
import glob
import pytest

from orm.core import manager, models


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

    def test_session_bind_added(self, engine):
        session = manager.Session(bind=engine)
        assert session.engine == engine

    def test_session_bind_added_through_configuration(self, engine):
        session = manager.Session()
        session.configure(bind=engine)
        assert session.engine == engine

    def test_table_created_through_session_instance(self, engine):
        session = manager.Session(bind=engine)
        user = User(name="Yeldos", email="yeldos@gmail.com")
        session.create_table(user)
        session.save()

        engine = manager.create_engine('sqlite.db')
        c = engine.cursor()
        name = c.execute(f'SELECT name FROM {user.__tablename__}')
        assert user.name.lower() in name.fetchone()

    def test_instance_added_through_session(self, engine):
        session = manager.Session(bind=engine)
        user = User(name="Yeldos", email="yeldos@gmail.com")
        session.add(user)
        session.save()

        engine = manager.create_engine('sqlite.db')
        c = engine.cursor()
        name = c.execute(f'SELECT name FROM {user.__tablename__}')
        assert user.name.lower() in name.fetchone()

    #
    # def test_query_db(self):
    #     pass

    # def test_create_table_success(self, engine):
    #     session = manager.Session(bind=engine)
    #     session.add(User())
    #     session.query(User())
