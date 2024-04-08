from telebot import types
from src.utils.emojis import *

# Markup example with rows
def menu_markup():
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(f"Menu button 1", callback_data=f'menu_button_1')
    item2 = types.InlineKeyboardButton(f"Menu button 2", callback_data=f'menu_button_2')
    item3 = types.InlineKeyboardButton(f"Bot help", callback_data=f'menu_button_help')
    item4 = types.InlineKeyboardButton(f"Contacts", callback_data=f'menu_button_contacts')
    markup.row(item1, item2, item3)
    markup.row(item4)
    return markup
