from app.database import RepController


class GetHistoryHandler:
    def __init__(self, bot) -> None:
        @bot.message_handler(
            commands=["h", "history"], chat_types=["group", "supergroup"]
        )
        def get_user_history(message):
            db = RepController()
            my_id = message.from_user.id

            if message.reply_to_message:
                user_id = message.reply_to_message.from_user.id

                if my_id != user_id:
                    h_text = ""
                    history = db.get_reduce_rep_history(user_id)

                    for record in history:
                        h_text += f"Reason: <b>{record.reason}</b>\nDate: <b>{record.date}</b>\n\n"

                    if history:
                        bot.reply_to(
                            message, "🗃 Reducing rep history of user:\n\n" + h_text
                        )
                        return
                    bot.reply_to(message, "❌ This user has not rep history!")
