from engine.mysql import mysql_connection_pool
from models.board import BoardModel
from exception import InvalidParam, ServerError, NotFoundContent, DEFINED_EXCEPTIONS
from common.pagination import OffsetPagination


class BoardService:
    @staticmethod
    def create_board(data):
        session = mysql_connection_pool.get_connection()
        try:
            BoardModel.create_board(session=session, data=data)
            session.commit()
            return True

        except Exception as e:
            if any([isinstance(e, exc) for exc in DEFINED_EXCEPTIONS]):
                raise e
            raise ServerError(reason='서버 오류가 발생 했습니다.')

        finally:
            session.close()

    @staticmethod
    def update_board(board_id, data):
        session = mysql_connection_pool.get_connection()
        try:
            BoardModel.update_board(session=session, board_id=board_id, data=data)
            session.commit()
            return True

        except Exception as e:
            if any([isinstance(e, exc) for exc in DEFINED_EXCEPTIONS]):
                raise e
            raise ServerError(reason='서버 오류가 발생 했습니다.')

        finally:
            session.close()

    @staticmethod
    def delete_board(board_id):
        session = mysql_connection_pool.get_connection()
        try:
            BoardModel.delete_board(session=session, board_id=board_id)
            session.commit()
            return True

        except Exception as e:
            if any([isinstance(e, exc) for exc in DEFINED_EXCEPTIONS]):
                raise e
            raise ServerError(reason='서버 오류가 발생 했습니다.')

        finally:
            session.close()

    @staticmethod
    def get_board(board_id):
        session = mysql_connection_pool.get_connection()
        try:
            board = BoardModel.get_board(session=session, board_id=board_id)
            if board is None:
                raise NotFoundContent(reason='게시글이 없습니다.')

            return board

        except Exception as e:
            if any([isinstance(e, exc) for exc in DEFINED_EXCEPTIONS]):
                raise e
            raise ServerError(reason='서버 오류가 발생 했습니다.')

        finally:
            session.close()

    @staticmethod
    def get_boards(params):
        session = mysql_connection_pool.get_connection()
        try:
            queryset = session.query(BoardModel).filter(BoardModel.is_deleted == False)

            writer = params.get('writer')
            title = params.get('title')

            if writer is not None:
                queryset = queryset.filter(BoardModel.writer.like(f'%{writer}%'))
            if title is not None:
                queryset = queryset.filter(BoardModel.title.like(f'%{title}%'))

            pagination, result = OffsetPagination(
                model=BoardModel,
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
