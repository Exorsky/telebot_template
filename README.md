### Features

- Easy to use structure. All files are in different folders
- Thats all :)

### To-Do
- Add database connection template (at least sqlite3)

### Project structure
Directory path  | For what its used
------------- | -------------
src/callbacks  | Bot callback functions
src/cmds/user  | Uuer only command functions
src/cmds/admin  | Admin only command functions
src/filters  | Custom filters. For example, admin check
src/handlers | Register command and callback handlers.
src/logger | Logger setup file
src/markups | Custom markups which could be replied in messages
src/middlewares | Custom middlewares, for example, antispam
src/utils/emojis | Emojis used for text decoration
src/utis/texts | Texts used for bot messages or markup

### Setup
```
git clone https://github.com/Exorsky/telebot_template.git
pip install -r requirements.txt
Add your bot token in config.yaml file
```

### How to add admin previleges
```
Add your int(user_id) in config.yaml Admins list
```
