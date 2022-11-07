from .bot import TelegramBot
from .handlers import MessageHandler


bot = TelegramBot()

MessageHandler(bot)

bot.start()