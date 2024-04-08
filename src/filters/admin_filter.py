import yaml
from telebot.custom_filters import SimpleCustomFilter

class AdminFilter(SimpleCustomFilter):
    key = 'admin'
    def __init__(self):
        super().__init__()
        self.admin_chat_ids = self.load_admin_chat_ids()

    def load_admin_chat_ids(self):
        # Load configuration
        with open('config.yaml', 'r') as file:
            config = yaml.safe_load(file)
        return config.get('Telegram', {}).get('Bot', {}).get('Admins', [])

    def check(self, message):
        return int(message.chat.id) in self.admin_chat_ids
