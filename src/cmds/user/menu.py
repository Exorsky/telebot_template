from telebot import TeleBot
from telebot.types import Message
from src.markups.menu_markup import menu_markup

def menu(message: Message, bot: TeleBot):
    bot.send_message(message.chat.id, "Here is simple bot menu", reply_markup=menu_markup())