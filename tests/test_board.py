from http import HTTPStatus

from . import BaseTestCase


class TestBoard(BaseTestCase):
    board_id = 1

    def test_create_board(self):
        data = {
            "title": "테스트 제목",
            "content": "테스트 내용",
            "writer": "테스트 작성자",
            "password": "테스트 비밀번호"
        }

        res = self.app.post('/boards', json=data)
        assert res.status_code == HTTPStatus.OK

    def test_update_board(self):
        self.test_create_board()
        data = {
            "title": "수정된 테스트 제목",
            "content": "수정된 테스트 내용",
            "writer": "수정된 테스트 작성자",
            "password": "수정된 테스트 비밀번호"
        }

        res = self.app.put('/boards/1', json=data)
        assert res.status_code == HTTPStatus.OK

    def test_delete_board(self):
        self.test_create_board()
        res = self.app.delete(f'/boards/{self.board_id}')
        assert res.status_code == HTTPStatus.OK

    def test_get_board(self):
        self.test_create_board()
        res = self.app.get(f'/boards/{self.board_id}')
        assert res.status_code == HTTPStatus.OK

    def test_get_boards(self):
        self.test_create_board()
        res = self.app.get(f'/boards')
        assert res.status_code == HTTPStatus.OK
