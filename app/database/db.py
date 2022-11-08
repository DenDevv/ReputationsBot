from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()
Session = sessionmaker()
engine = create_engine("sqlite:///database.db?check_same_thread=False")