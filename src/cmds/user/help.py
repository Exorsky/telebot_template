from telebot import TeleBot
from telebot.types import Message

def help(message: Message, bot: TeleBot):
    bot.send_message(message.chat.id, "Here is bot help")