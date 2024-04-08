from telebot.types import Message
from telebot import TeleBot
from src.logger.logger import configure_logger
from src.utils.texts import spam_warning_text
import time

# Get logger
logger = configure_logger()

DATA = {}

def antispam_checker(bot: TeleBot, message: Message):
    bot.temp_data = {message.from_user.id : 'OK'}
    if DATA.get(message.from_user.id):
        if int(time.time()) - DATA[message.from_user.id] < 2:
            bot.temp_data = {message.from_user.id : 'FAIL'}
            bot.send_message(message.chat.id, spam_warning_text())
            logger.warning(f"User {message.chat.id}#{message.from_user.username} is spamming with text '{message.text}'")
    DATA[message.from_user.id] = message.date