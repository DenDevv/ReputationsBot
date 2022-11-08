import telebot
from typing import List
from config import config
from app.database import engine, Base
from app.handlers import MessageHandler


# Create a database table
# Base.metadata.create_all(engine)


class TelegramBot:
    def __init__(self) -> None:
        self.bot = telebot.TeleBot(config.BOT_TOKEN)
        self.bot.parse_mode = "html"
        MessageHandler(self.bot)

    def start(self):
        self.bot.infinity_polling()

    def add_command_handler(self, commands: List[str], callback):
        self.bot.register_message_handler(
            callback=callback,
            commands=commands
        )