import re
import os
from os import environ, getenv
from Script import script

# Utility functions
id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# ============================
# Bot Information Configuration
# ============================
SESSION = environ.get('SESSION', 'dreamxbotz_search')
API_ID = int(environ.get('API_ID', '12334596'))
API_HASH = environ.get('API_HASH', '47071ddd4d2461be0a007a0f95f59fa8')
BOT_TOKEN = environ.get('BOT_TOKEN', "6713190956:AAGAerjKcMQII9Nuozp9Q0s73RtvCQNor8g")

# ============================
# Admin Configuration
# ============================
# നിങ്ങളുടെ ഐഡി ഇവിടെ ചേർത്തിട്ടുണ്ട്
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1209407849').split()]

# ============================
# MongoDB Configuration
# ============================
# Empty Host എറർ വരാതിരിക്കാൻ ലിങ്ക് കൃത്യമായി നൽകിയിട്ടുണ്ട്
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://igv2luro:igv2luro@cluster0.p0kopsa.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'dreamcinezone_files')

# ============================
# Bot Settings
# ============================
PORT = int(environ.get("PORT", "10000"))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002117429873'))
DELETE_TIME = int(environ.get("DELETE_TIME", "300"))
IMDB = is_enabled((environ.get('IMDB', "False")), False)
PM_SEARCH = bool(environ.get('PM_SEARCH', True))
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)

# ============================
# Server Configuration
# ============================
# Render-ൽ ക്രാഷ് ആകാതിരിക്കാൻ ലളിതമായ സെർവർ സെറ്റിംഗ്സ്
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS))
URL = "http://{}/".format(FQDN)

# ============================
# Commands Bot
# ============================
Bot_cmds = {
    "start": "Start the Bot",
    "stats": "Get Bot Stats",
    "alive": "Check Bot Alive Status",
    "restart": "Restart Bot"
}

LOG_STR = "Bot Configurations are active.\n"
