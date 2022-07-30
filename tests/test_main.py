from http import HTTPStatus

from . import BaseTestCase


class TestMain(BaseTestCase):
    def test_main(self):
        rv = self.app.get('/')
        assert rv.status_code == HTTPStatus.OK
