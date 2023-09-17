from pyrogram import Client, filters
from pyrogram.handlers.message_handler import MessageHandler
from pyrogram.types import Message 
import logging
from data import check_user
import sys

api_id = 000000
api_hash = "xxx9c9x9cz9jafafdfdf"


client = Client(name="account_data", api_id=api_id, api_hash=api_hash)


logging.basicConfig(level=logging.INFO, filename="app.log", filemode="w", encoding="utf-8", format="%(filename)s[%(funcName)s]: %(message)s")

stream_handler = logging.StreamHandler(stream=sys.stdout)
stream_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(filename)s[%(funcName)s]: %(message)s")
stream_handler.setFormatter(formatter)


logger = logging.getLogger("AutoResponse")
logger.addHandler(stream_handler)

def auto_response(client: Client, message: Message):
    if check_user(message.from_user.id):
        user = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        logger.info(f"Приветственное сообщение отправлено в чат с {user} ({message.from_user.id})")
        message.reply(f"Привет! @{message.from_user.username}")
    else:
        user = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        logger.warn(f"Пользователь {user} ({message.from_user.id}) уже есть в истории чата...")

client.add_handler(MessageHandler(auto_response, filters.private))

if __name__ == "__main__":
    client.run()
