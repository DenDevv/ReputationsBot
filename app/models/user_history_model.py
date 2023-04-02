from datetime import datetime
from sqlalchemy import Column, BigInteger, Integer, String, DateTime

from config import config


dev_config = config.get("development")


class UserRepHistory(dev_config.Base):
    __tablename__ = "user_rep_history"
    id = Column(Integer(), primary_key=True)
    user_id = Column(BigInteger(), nullable=False)
    reason = Column(String(255), nullable=False)
    date = Column(
        DateTime, server_default=datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
    )
