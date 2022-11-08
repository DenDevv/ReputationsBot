from app.database import RepController


class MessageHandler:
    def __init__(self, bot) -> None:
        self.rep_up = ["+rep", "+реп", "+r", "+р"]
        self.rep_down = ["-rep", "-реп", "-r", "-р"]
        self.info = ["!rep", "!реп", "!r", "!р", "!info"]

        @bot.message_handler(content_types=['text'])
        def messages(message):
            db = RepController()
            msg = message.text
            chat_id = message.chat.id
            my_id = message.from_user.id
            bot_id = 5714569779

            if message.chat.type != "private":
                if not db.get_user(my_id):
                    db.add_new_user(my_id)

                if message.reply_to_message:
                    user_id = message.reply_to_message.from_user.id
                    user_fname = bot.get_chat_member(chat_id, user_id).user.first_name

                    if my_id != user_id and bot_id != user_id:
                        if not db.get_user(user_id):
                            db.add_new_user(user_id)

                        if msg in self.rep_up:
                            db.increase_rep(user_id)
                            bot.reply_to(
                                message,
                                f"📈 Reputation for <b>{user_fname}</b>, has been increased!"
                            )

                        if msg in self.rep_down:
                            if db.get_rep(my_id) >= 15:
                                db.reduce_rep(user_id)
                                bot.reply_to(
                                    message,
                                    f"📉 Reputation for <b>{user_fname}</b>, has been reduced!"
                                )

                        if msg in self.info:
                            bot.reply_to(
                                message,
                                f"📊 Reputation of <b>{user_fname}</b>: {db.get_rep(user_id)}🌟"
                        )
                    return

                if msg in self.info:
                    bot.reply_to(
                        message,
                        f"📊 Your reputation: {db.get_rep(my_id)}🌟"
                )
