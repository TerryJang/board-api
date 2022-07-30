from engine.mysql import mysql_connection_pool
from models.comment import CommentModel
from exception import InvalidParam, ServerError, DEFINED_EXCEPTIONS


class CommentService:
    @staticmethod
    def create_comment(board_id, data):
        session = mysql_connection_pool.get_connection()
        try:
            data['board_id'] = board_id
            CommentModel.create_comment(session=session, data=data)
            session.commit()
            return True

        except Exception as e:
            if any([isinstance(e, exc) for exc in DEFINED_EXCEPTIONS]):
                raise e
            raise ServerError(reason='서버 오류가 발생 했습니다.')

        finally:
            session.close()

    @staticmethod
    def get_comments(board_id):
        session = mysql_connection_pool.get_connection()
        try:
            return CommentModel.get_comments(session=session, board_id=board_id)

        except Exception as e:
            if any([isinstance(e, exc) for exc in DEFINED_EXCEPTIONS]):
                raise e
            raise ServerError(reason='서버 오류가 발생 했습니다.')

        finally:
            session.close()
