from sqlalchemy import Column, BigInteger, Integer

from app.database import Base


class UserReps(Base):
    __tablename__ = "user_reps"
    id = Column(Integer(), primary_key=True)
    user_id = Column(BigInteger(), nullable=False, unique=True)
    reputation = Column(Integer(), nullable=False)