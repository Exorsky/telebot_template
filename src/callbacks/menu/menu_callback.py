from telebot import TeleBot
from telebot.types import CallbackQuery
from src.cmds.user.help import help as help_cmd

def menu_callback(callback_query: CallbackQuery, bot : TeleBot):
    # Process the callback query
    cb = callback_query.data

    if cb == 'menu_button_1':
        bot.send_message(callback_query.message.chat.id, "You selected option 1")

    if cb == 'menu_button_2':
        bot.send_message(callback_query.message.chat.id, "You selected option 2")

    if cb == 'menu_button_help':
        from src.utils.texts import help_text
        bot.send_message(callback_query.message.chat.id, help_text())

    if cb == 'menu_button_contacts':
        from src.utils.texts import menu_contacts_text
        bot.send_message(callback_query.message.chat.id, menu_contacts_text())

