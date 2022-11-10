from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


test_base = declarative_base()
test_session = sessionmaker()
test_engine = create_engine("sqlite:///tests/test_data.db?check_same_thread=False")
test_base.metadata.create_all(test_engine)