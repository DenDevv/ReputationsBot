import telebot
from config import config
from app.handlers import MessageHandler, JoinedUserHandler, GetHistoryHandler


dev_config = config.get("development")
base_config = config.get("base")

# Create a database table
dev_config.Base.metadata.create_all(dev_config.engine)


class TelegramBot:
    def __init__(self) -> None:
        self.bot = telebot.TeleBot(base_config.BOT_TOKEN)
        self.bot.parse_mode = "html"
        GetHistoryHandler(self.bot)
        MessageHandler(self.bot)
        JoinedUserHandler(self.bot)

    def start(self):
        self.bot.infinity_polling()