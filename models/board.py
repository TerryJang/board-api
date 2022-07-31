from datetime import datetime

from engine.mysql import Base
from sqlalchemy import Column, BigInteger, String, DateTime, Boolean, func


class BoardModel(Base):
    __tablename__ = 'board'

    id = Column(BigInteger, primary_key=True, autoincrement=True, comment='아이디')
    title = Column(String(255), comment='제목')
    content = Column(String(255), comment='내용')
    writer = Column(String(255), comment='작성자')
    password = Column(String(255), comment='비밀번호')
    is_deleted = Column(Boolean, default=False, comment='삭제여부')
    deleted_at = Column(DateTime, comment='삭제일')
    created_at = Column(DateTime, default=func.now(), comment='생성일')
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), comment='변경일')

    @staticmethod
    def create_board(session, data):
        board = BoardModel(**data)
        session.add(board)
        return True

    @staticmethod
    def update_board(session, board_id, data):
        session.query(BoardModel).filter(BoardModel.id == board_id).update(data)
        return True

    @staticmethod
    def delete_board(session, board_id):
        now = datetime.now()
        data = {
            "is_deleted": True,
            "deleted_at": now
        }
        session.query(BoardModel).filter(BoardModel.id == board_id).update(data)
        return True

    @staticmethod
    def get_boards(session):
        return session.query(BoardModel).filter(BoardModel.is_deleted == False).all()

    @staticmethod
    def get_board(session, board_id):
        return session.query(BoardModel).filter(BoardModel.id == board_id, BoardModel.is_deleted == False).first()
