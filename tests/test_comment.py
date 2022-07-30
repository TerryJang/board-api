from http import HTTPStatus

from . import BaseTestCase
from .test_board import TestBoard


class TestComment(BaseTestCase):
    board_id = 1

    def test_create_comment(self):
        board_data = {
            "title": "테스트 제목",
            "content": "테스트 내용",
            "writer": "테스트 작성자",
            "password": "테스트 비밀번호"
        }
        board_res = self.app.post('/boards', json=board_data)
        assert board_res.status_code == HTTPStatus.OK

        comment_data = {
            "content": "테스트 댓글 내용",
            "writer": "테스트 댓글 작성자",
            "password": "테스트 댓글 비밀번호"
        }

        comment_res = self.app.post(f'/boards/{self.board_id}/comments', json=comment_data)
        assert comment_res.status_code == HTTPStatus.OK

    def test_get_boards(self):
        self.test_create_comment()

        res = self.app.get(f'/boards/{self.board_id}/comments')
        assert res.status_code == HTTPStatus.OK
