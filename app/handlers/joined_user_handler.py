from app.database import RepController
from config import config


dev_config = config.get("development")


class JoinedUserHandler:
    def __init__(self, bot) -> None:
        @bot.message_handler(content_types=['new_chat_members'])
        def new_chat_member(message):
            db = RepController()
            new = message.new_chat_members[0]
            user_id = new.id
            first_name = new.first_name or '-'
            last_name = new.last_name or '-'
            username = "@" + new.username if new.username else "-"
            is_bot = new.is_bot

            if db.get_user(user_id):
                rep = db.get_rep(user_id)
                if rep <= -10:
                    bot.reply_to(
                        message, 
                        dev_config.attention_text.format(
                            rep, first_name, last_name,
                            username, is_bot, user_id
                        )
                    )
                return
            db.add_new_user(user_id)                