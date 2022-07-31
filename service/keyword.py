from engine.mysql import mysql_connection_pool
from models.keyword import KeywordModel
from exception import InvalidParam, ServerError, DEFINED_EXCEPTIONS


class KeywordService:
    @staticmethod
    def send_keyword_notification(text):
        session = mysql_connection_pool.get_connection()
        try:
            keyword_list = text.split()

            for keyword in keyword_list:
                writers = KeywordModel.get_writer_by_keyword(session, keyword)

                for writer in writers:
                    KeywordService.send_notification(writer=writer)

            return True

        except Exception as e:
            if any([isinstance(e, exc) for exc in DEFINED_EXCEPTIONS]):
                raise e
            raise ServerError(reason='서버 오류가 발생 했습니다.')

        finally:
            session.close()

    @staticmethod
    def send_notification(writer):
        pass
