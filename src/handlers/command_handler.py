from telebot import TeleBot
from telebot.types import Message

# Commands which are available for all users
def register_user_handlers(bot):
    from src.cmds.user.start import start as start_cmd
    from src.cmds.user.menu import menu as menu_cmd
    from src.cmds.user.help import help as help_cmd

    bot.register_message_handler(start_cmd, commands=['start'], pass_bot=True)
    bot.register_message_handler(menu_cmd, commands=['menu'], pass_bot=True)
    bot.register_message_handler(help_cmd, commands=['help'], pass_bot=True)

# Command which are available only for admins
# Should have admin=True key to make command available for admins
def register_admin_handlers(bot):
    from src.cmds.admin.general import test_admin as test_admin_cmd
    from src.cmds.admin.general import show_raw_message as show_raw_message_cmd

    bot.register_message_handler(test_admin_cmd,  admin=True, commands=['testadmin'], pass_bot=True)
    bot.register_message_handler(show_raw_message_cmd,  admin=True, commands=['raw'], pass_bot=True)