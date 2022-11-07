from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()
Session = sessionmaker()
engine = create_engine("sqlite:///app/database/database.db", echo=True)