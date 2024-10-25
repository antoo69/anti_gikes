import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

load_dotenv(".env")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7619388917:AAFVQCD9u_2fKYFznCvdUZA21OyY_9bkbtU")
BOT_WORKERS = int(os.environ.get("BOT_WORKERS", "4"))

APP_ID = int(os.environ.get("APP_ID", "22355402"))
API_HASH = os.environ.get("API_HASH", "5d7858e035599aa080d65e14e5e34d4d")

LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID", "-1002057319198"))

MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://ferdisyrl:buburayam1@cluster0.89myp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "ferdisyrl")
BROADCAST_AS_COPY = False

PLUG = dict(root="antigcast/plugins")

OWNER_ID = [int(x) for x in (os.environ.get("OWNER_ID", "7083782157 1506963557").split())]
OWNER_NAME = os.environ.get("OWNER_NAME", "@fsyrl @fsyrl9")


LOG_FILE_NAME = "antigcast_logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
