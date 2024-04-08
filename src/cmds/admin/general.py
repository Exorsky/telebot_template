from telebot import TeleBot
from telebot.types import Message
from src.utils.emojis import elite

def test_admin(message: Message, bot: TeleBot):
    bot.send_message(message.chat.id, f"{elite} You are admin of this bot")

def show_raw_message(message: Message, bot: TeleBot):
    bot.send_message(message.chat.id, str(message))
    print(str(message))