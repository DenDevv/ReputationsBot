import os
import pytest
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))


@pytest.fixture
def drop_tables():
    TestingConfig.Base.metadata.drop_all(TestingConfig.engine)
    TestingConfig.Base.metadata.create_all(TestingConfig.engine)


class BaseConfig:
    """Base configuration."""

    BOT_TOKEN = os.environ.get("TOKEN")


class DevelopmentConfig:
    """Development configuration."""

    Base = declarative_base()
    Session = sessionmaker()
    engine = create_engine(
        "sqlite:///app/database/database.db?check_same_thread=False"
    )

    bot_id = 5714569779

    attention_text = """⚠️ Attention! Joined user with overlow reputation! ⚠️

📊 Reputation: <i>{0}</i> 🌟

🔗 First name: <u>{1}</u>
🔗 Last name: <u>{2}</u>
🔖 Username: {3}
🤖 Is bot: <b>{4}</b>

🆔 <code>{5}</code>"""


class TestingConfig:
    """Testing configuration."""

    Base = declarative_base()
    Session = sessionmaker()
    engine = create_engine(
        "sqlite:///app/database/database.db?check_same_thread=False"
    )


config = dict(
    base=BaseConfig,
    development=DevelopmentConfig, 
    testing=TestingConfig
)