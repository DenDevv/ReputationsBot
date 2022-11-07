from app.bot import TelegramBot
from app.database import RepController


class MessageHandler:
    def __init__(self, bot_instance: TelegramBot) -> None:
        self.rep_up = ["+rep", "+реп", "+r", "+р"]
        self.rep_down = ["-rep", "-реп", "-r", "-р"]
        self.info = ["!rep", "!реп", "!r", "!р", "!info"]

        def messages(message):
            db = RepController()
            msg = message.text
            chat_id = message.chat.id
            my_id = message.from_user.id
            user_id = message.reply_to_message.from_user.id
            user_fname = bot_instance.bot.get_chat_member(chat_id, user_id).user.first_name

            if not db.get_rep(user_id):
                db.add_new_user(user_id)

            if message.reply_to_message:
                if msg in self.rep_up:
                    db.increase_rep(user_id)
                    bot_instance.bot.send_message(
                        chat_id, 
                        f"📈 Reputation for <b>{user_fname}</b>, has been increased!"
                    )
                    return

                if msg in self.rep_down:
                    if db.get_rep(my_id) >= 15:
                        db.reduce_rep(user_id)
                        bot_instance.bot.send_message(
                            chat_id, 
                            f"📉 Reputation for <b>{user_fname}</b>, has been reduced!"
                        )
                    return
                
                if msg in self.info:
                    bot_instance.bot.send_message(
                        chat_id, 
                        f"📉 Reputation of <b>{user_fname}</b>: {db.get_rep(user_id)}🌟"
                    )
                    return

        bot_instance.add_content_type_handler(
            content_types=['text'],
            callback=messages
        )
