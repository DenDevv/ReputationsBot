from sqlalchemy import Column, BigInteger, Integer

from config import config


dev_config = config.get("development")


class UserReps(dev_config.Base):
    __tablename__ = "user_reps"
    id = Column(Integer(), primary_key=True)
    user_id = Column(BigInteger(), nullable=False, unique=True)
    reputation = Column(Integer(), nullable=False)