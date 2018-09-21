import os
import glob
import pytest

from orm.core import manager


class TestORM:

    def test_engine_created_success(self):
        db_name = 'sqlite.db'
        manager.create_engine(db_name)
        assert db_name in glob.glob('*')