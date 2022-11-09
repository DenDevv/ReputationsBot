from datetime import datetime
from sqlalchemy import Column, BigInteger, Integer, String, DateTime

from app.database import Base


class UserRepHistory(Base):
    __tablename__ = "user_rep_history"
    id = Column(Integer(), primary_key=True)
    user_id = Column(BigInteger(), nullable=False, unique=True)
    reason = Column(String(255), nullable=False)
    date = Column(DateTime, server_default=datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"))