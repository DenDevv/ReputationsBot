import telebot
from config import config
from app.database import engine, Base
from app.handlers import MessageHandler, JoinedUserHandler, GetHistoryHandler


# Drop a database for tests!
Base.metadata.drop_all(bind=engine)

# Create a database table
Base.metadata.create_all(engine)


class TelegramBot:
    def __init__(self) -> None:
        self.bot = telebot.TeleBot(config.BOT_TOKEN)
        self.bot.parse_mode = "html"
        GetHistoryHandler(self.bot)
        MessageHandler(self.bot)
        JoinedUserHandler(self.bot)

    def start(self):
        self.bot.infinity_polling()