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
# Admin, Channels & Users Configuration
# ============================
# ADMINS ലിസ്റ്റിൽ നിങ്ങളുടെ ഐഡി ചേർത്തു
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1209407849').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-100').split()]

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002117429873'))
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1002117429873'))
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-1002076177450'))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-100').split()]
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1002076177450')
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1002076177450')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/mudiyanmass')

# FORCE_SUB 
auth_req_channels = environ.get("AUTH_REQ_CHANNELS", "-1002076177450")
auth_channels     = environ.get("AUTH_CHANNELS", "-1002076177450")

# ============================
# Payment Configuration
# ============================
QR_CODE = environ.get('QR_CODE', 'https://graph.org/file/56b5deb73f3b132e2bb73.jpg')
OWNER_UPI_ID = environ.get('OWNER_UPI_ID', 'No Available')

STAR_PREMIUM_PLANS = {
    10: "7day",
    20: "15day",    
    40: "1month", 
    55: "45day",
    75: "60day",
}

# ============================
# MongoDB Configuration
# ============================
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://igv2luro:igv2luro@cluster0.p0kopsa.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'dreamcinezone_files')

MULTIPLE_DB = is_enabled(os.environ.get('MULTIPLE_DB', "False"), False)
DATABASE_URI2 = environ.get('DATABASE_URI2', "")

# ============================
# Movie Notification & Update Settings
# ============================
MOVIE_UPDATE_NOTIFICATION = bool(environ.get('MOVIE_UPDATE_NOTIFICATION', False))
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-100'))
DREAMXBOTZ_IMAGE_FETCH = bool(environ.get('DREAMXBOTZ_IMAGE_FETCH', True))
LINK_PREVIEW = bool(environ.get('LINK_PREVIEW', False))
ABOVE_PREVIEW = bool(environ.get('ABOVE_PREVIEW', True))
TMDB_API_KEY = environ.get('TMDB_API_KEY', '')
TMDB_POSTER = bool(environ.get('TMDB_POSTER', False))
LANDSCAPE_POSTER = bool(environ.get('LANDSCAPE_POSTER', True))

# ============================
# Verification Settings
# ============================
IS_VERIFY = is_enabled('IS_VERIFY', False)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-100'))
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-100'))
VERIFY_IMG = environ.get("VERIFY_IMG", "https://telegra.ph/file/9ecc5d6e4df5b83424896.jpg")

TUTORIAL = environ.get("TUTORIAL", "https://t.me/mudiyanmass")
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://t.me/mudiyanmass")
TUTORIAL_3 = environ.get("TUTORIAL_3", "https://t.me/mudiyanmass")

SHORTENER_API = environ.get("SHORTENER_API", "a7ac9b3012c67d7491414cf272d82593c75f6cbb")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "omegalinks.in")

SHORTENER_API2 = environ.get("SHORTENER_API2", "a7ac9b3012c67d7491414cf272d82593c75f6cbb")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "omegalinks.in")

SHORTENER_API3 = environ.get("SHORTENER_API3", "a7ac9b3012c67d7491414cf272d82593c75f6cbb")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "omegalinks.in")

TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "1200"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "54000"))

# ============================
# Channel & Group Links Configuration
# ============================
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/mudiyanmass')
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/mudiyanmass')
UPDATE_CHNL_LNK = environ.get('UPDATE_CHNL_LNK', 'https://t.me/mudiyanmass')

# ============================
# User Configuration
# ============================
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '').split()]

# ============================
# Miscellaneous Configuration
# ============================
ULTRA_FAST_MODE = is_enabled(environ.get('ULTRA_FAST_MODE', "False"), True)

MAX_B_TN = environ.get("MAX_B_TN", "5")
PORT = int(environ.get("PORT", "10000"))
MSG_ALRT = environ.get('MSG_ALRT', 'Share & Support Us')
DELETE_TIME = int(environ.get("DELETE_TIME", "300"))
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True))
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
TMDB_ON_SEARCH = is_enabled((environ.get('TMDB_ON_SEARCH', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PM_SEARCH = bool(environ.get('PM_SEARCH', True))
EMOJI_MODE = bool(environ.get('EMOJI_MODE', False))
BUTTON_MODE = is_enabled((environ.get('BUTTON_MODE', "False")), False)
STREAM_MODE = bool(environ.get('STREAM_MODE', True))
PREMIUM_STREAM_MODE = bool(environ.get('PREMIUM_STREAM_MODE', False))

# ============================
# Server & Web Configuration
# ============================
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else "https://{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'dreamXBotz'))
MULTI_CLIENT = False
name = str(environ.get('name', 'DREAMXBOTZ'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))
HAS_SSL = bool(getenv('HAS_SSL', True))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)

# ============================
# Commands Bot
# ============================
Bot_cmds = {
    "start": "Start the Bot",
    "stats": "Get Bot Stats",
    "alive": "Check Bot Alive Status",
    "settings": "Change Settings",
    "id": "Get Telegram ID",
    "info": "Get User Info",
    "del_msg": "Remove File Name Collection Notification",
    "restart": "Restart Bot"
}

# ============================
# Logs Configuration
# ============================
LOG_STR = "Current Customized Configurations are active.\n"
