from src.utils.emojis import *
import yaml

# Load YAML configuration
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)


def help_text():
    return """
Here list of available commands:

/start - start/restart bot
/menu - show menu
/help - show help
"""

def spam_warning_text():
    return f"""{warning} You are making request too often"""

def menu_contacts_text():
    # Access bot information
    bot_name = config['Bot']['name']
    author_name = config['Bot']['author']
    author_email = config['Bot']['email']
    return f"""Author contact information:

    {bot_name}
    {author_name}
    {author_email}
    """