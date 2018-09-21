import pytest

from orm.core import manager


class TestORM:

    def test_engine_created_success(self):
        engine = create_engine()
