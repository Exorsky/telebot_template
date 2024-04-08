from telebot import TeleBot
from telebot.types import Message

def start(message: Message, bot: TeleBot):
    bot.send_message(message.chat.id, "Hello, user!")