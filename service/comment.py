from engine.mysql import mysql_connection_pool
from models.comment import CommentModel
from exception import InvalidParam, ServerError, DEFINED_EXCEPTIONS
from common.pagination import OffsetPagination


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
    def get_comments(board_id, params):
        session = mysql_connection_pool.get_connection()
        try:
            queryset = session.query(CommentModel).filter(
                CommentModel.board_id == board_id,
                CommentModel.is_deleted == False
            )

            pagination, result = OffsetPagination(
                model=CommentModel,
                queryset=queryset,
                size=params.get('size', 10),
                page=params.get('page', 1),
            ).paginate()

            return pagination, result

        except Exception as e:
            if any([isinstance(e, exc) for exc in DEFINED_EXCEPTIONS]):
                raise e
            raise ServerError(reason='서버 오류가 발생 했습니다.')

        finally:
            session.close()
