from engine.mysql import Base
from sqlalchemy import Column, BigInteger, String, DateTime, func


class KeywordModel(Base):
    __tablename__ = 'keyword'

    id = Column(BigInteger, primary_key=True, autoincrement=True, comment='아이디')
    writer = Column(String(255), comment='작성자')
    keyword = Column(String(255), comment='키워드')
    created_at = Column(DateTime, default=func.now(), comment='생성일')

    @staticmethod
    def get_writer_by_keyword(session, keyword):
        return session.query(KeywordModel).filter(KeywordModel.keyword == keyword).all()
