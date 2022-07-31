from datetime import datetime

from engine.mysql import Base
from sqlalchemy import Column, BigInteger, String, DateTime, Boolean, func, ForeignKey


class CommentModel(Base):
    __tablename__ = 'comment'

    id = Column(BigInteger, primary_key=True, autoincrement=True, comment='아이디')
    board_id = Column(BigInteger, ForeignKey("board.id"), comment='게시판 글 아이디')
    parent = Column(BigInteger, comment='댓글 아이디')
    content = Column(String(255), comment='내용')
    writer = Column(String(255), comment='작성자')
    password = Column(String(255), comment='비밀번호')
    is_deleted = Column(Boolean, default=False, comment='삭제여부')
    deleted_at = Column(DateTime, comment='삭제일')
    created_at = Column(DateTime, default=func.now(), comment='생성일')
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), comment='변경일')

    @staticmethod
    def create_comment(session, data):
        board = CommentModel(**data)
        session.add(board)
        return True

    @staticmethod
    def get_comments(session, board_id):
        return session.query(CommentModel).filter(CommentModel.board_id == board_id).all()
