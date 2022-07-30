import os
import unittest
from http import HTTPStatus

from sqlalchemy.orm.session import close_all_sessions
from sqlalchemy import BigInteger
from sqlalchemy.ext.compiler import compiles

from engine.mysql import mysql_connection_pool, Base
from settings import get_config


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['APPLICATION_ENV'] = 'test'
        from main import app
        self.app = app.test_client()

        config = get_config()
        mysql_connection_pool.setup(config)
        for table in Base.__subclasses__():
            table.__table__.create(bind=mysql_connection_pool.engine, checkfirst=True)

    @compiles(BigInteger, 'sqlite')
    def compile_BIGINTEGER(element, compiler, **kw):
        return compiler.visit_integer(element, **kw)

    def tearDown(self):
        close_all_sessions()
        Base.metadata.drop_all(bind=mysql_connection_pool.engine)
        del self.app

    def test_main(self):
        rv = self.app.get('/')
        assert rv.status_code == HTTPStatus.OK