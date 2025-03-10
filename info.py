import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'F2L')
API_ID = int(environ.get('API_ID', '26728872'))
API_HASH = environ.get('API_HASH', '96985c2aaea6c75408528909b7e18879')
BOT_TOKEN = environ.get('BOT_TOKEN', "7512502745:AAFJMb_sVQx8_vejyv0xbBY26W8i3D3OzEo")

# Bot settings
PORT = environ.get("PORT", "8080")

# Online Stream and Download
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "https://tasteless-aurore-rachel-24-4b0c1a09.koyeb.app/")

# Admins, Channels & Users
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002458319512'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1705634892').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://telegramguy21:tnkIwvbNkJ5U3fZ7@botsuse.bpgag.mongodb.net/?retryWrites=true&w=majority&appName=Botsuse")
DATABASE_NAME = environ.get('DATABASE_NAME', "tgktnsnsn")

# Shortlink Info
SHORTLINK = bool(environ.get('SHORTLINK', False)) # Set True Or False
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'api.shareus.io')
SHORTLINK_API = environ.get('SHORTLINK_API', 'hRPS5vvZc0OGOEUQJMJzPiojoVK2')
