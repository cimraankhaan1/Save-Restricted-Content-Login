import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7944829789:AAFfij6TA5H0WJiMscxVbGEytxXMz0A4KuY")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "17461958"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "0f083cb4779252f82b99f5c644274624")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "2081516065"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://khaanbarwaani:qL47JyUNrzSRp2Aj@cluster0.qgucx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "khaanbarwaani")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
