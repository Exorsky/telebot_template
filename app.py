import yaml
import telebot
from telebot import apihelper
apihelper.ENABLE_MIDDLEWARE = True

# Load config file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Bot constants
TOKEN = config['Telegram']['Bot']['token']
BOT_NAME = config['Bot']['name']

if TOKEN == "ENTER_YOUR_BOT_TOKEN":
    print("Please enter your bot token in config.yaml file")
    exit()

# Initialize the bot
bot = telebot.TeleBot(TOKEN)

# Get logger
from src.logger.logger import configure_logger
logger = configure_logger()

from src.utils.database import SQLiteDB
db = SQLiteDB("database.db")
conn,cursor = db.connect()

# Command handlers registartion
# New comands should be added to these handlers
from src.handlers.command_handler import register_admin_handlers,register_user_handlers
register_admin_handlers(bot)
register_user_handlers(bot)

# Callback handlers registartion
# New callbacks should be added to these handlers
from src.handlers.callback_handler import register_callback_handlers
register_callback_handlers(bot)

# Middlewares
from src.middlewares.antispam import antispam_checker
bot.register_middleware_handler(antispam_checker, update_types=['message'])

# Filter for admin only commands
# Admins could be added in config.yaml file
from src.filters.admin_filter import AdminFilter
bot.add_custom_filter(AdminFilter())

# Start the bot
logger.info(f"Bot '{BOT_NAME}' started")
bot.polling()

# Stop the bot
logger.warning(f"Bot '{BOT_NAME}' has been stopped")
