from telebot import TeleBot
from telebot.types import CallbackQuery
from functools import partial

def register_callback_handlers(bot):
    from src.callbacks.menu.menu_callback import menu_callback

    # Register the callback query handlers
    bot.register_callback_query_handler("menu_callback", lambda query: menu_callback(query, bot), pass_bot=True)

