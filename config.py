import os
from dotenv import load_dotenv


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))


class Config:
    BOT_TOKEN = os.environ.get("TOKEN")
    attention_text = """⚠️ Attention! Joined user with overlow reputation! ⚠️

📊 Reputation: <i>{0}</i> 🌟

🔗 First name: <u>{1}</u>
🔗 Last name: <u>{2}</u>
🔖 Username: {3}
🤖 Is bot: <b>{4}</b>

🆔 <code>{5}</code>"""


config = Config()