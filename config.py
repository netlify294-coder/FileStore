import os
import json
import logging
from logging.handlers import RotatingFileHandler

# Bot Configuration
LOG_FILE_NAME = "bot.log"
PORT = os.getenv("PORT", "5010")
OWNER_ID = int(os.getenv("OWNER_ID", "6497757690"))

MSG_EFFECT = int(os.getenv("MSG_EFFECT", "5046509860389126442"))

SHORT_URL = os.getenv("SHORT_URL", "linkshortify.com")  # shortner url
SHORT_API = os.getenv("SHORT_API", "")
SHORT_TUT = os.getenv("SHORT_TUT", "https://t.me/How_to_Download_7x/26")

# Bot Configuration
SESSION = os.getenv("SESSION", "yato")
TOKEN = os.getenv("TOKEN", "")
API_ID = os.getenv("API_ID", "")
API_HASH = os.getenv("API_HASH", "")
WORKERS = int(os.getenv("WORKERS", "5"))

DB_URI = os.getenv("DB_URI", "")
DB_NAME = os.getenv("DB_NAME", "yato")

# Force Subscription Channels [channel_id, request_enabled, timer_in_minutes]
# Set as JSON in the FSUBS env var, e.g. [[-1001234567890, true, 10]]
# Leave unset (or "[]") to disable force-subscribe.
FSUBS = json.loads(os.getenv("FSUBS", "[]"))

# Database Channel (Primary) — the private channel the bot stores files in
DB_CHANNEL = int(os.getenv("DB_CHANNEL", "0"))

# Multiple Database Channels (can be set via bot settings)
# DB_CHANNELS = {
#     "-1002595092736": {"name": "Primary DB", "is_primary": True, "is_active": True},
#     "-1001234567890": {"name": "Secondary DB", "is_primary": False, "is_active": True}
# }

# Auto Delete Timer (seconds)
AUTO_DEL = int(os.getenv("AUTO_DEL", "300"))

# Admin IDs — comma-separated in the ADMINS env var, e.g. "6123456789,9876543210"
ADMINS = [int(x) for x in os.getenv("ADMINS", "").split(",") if x.strip()]

# Bot Settings
DISABLE_BTN = os.getenv("DISABLE_BTN", "True") == "True"
PROTECT = os.getenv("PROTECT", "True") == "True"

# One-time batch (free trial) access button — shown when a user re-opens
# a batch link they've already used once
TRIAL_BTN_TEXT = os.getenv("TRIAL_BTN_TEXT", "💎 Get Premium")
TRIAL_BTN_URL = os.getenv("TRIAL_BTN_URL", "https://t.me/your_channel_or_bot")

# Messages Configuration
MESSAGES = {
    "START": "<b>›› ʜᴇʏ!!, {first} ~ <blockquote>ʟᴏᴠᴇ ᴘᴏʀɴʜᴡᴀ? ɪ ᴀᴍ ᴍᴀᴅᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ғɪɴᴅ ᴡʜᴀᴛ ʏᴏᴜ aʀᴇ ʟᴏᴏᴋɪɴɢ ꜰᴏʀ.</blockquote></b>",
    "FSUB": "<b><blockquote>›› ʜᴇʏ ×</blockquote>\n  ʏᴏᴜʀ ғɪʟᴇ ɪs ʀᴇᴀᴅʏ ‼️ ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ sᴜʙsᴄʀɪʙᴇᴅ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, sᴜʙsᴄʀɪʙᴇ ɴᴏᴡ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇs</b>",
    "ABOUT": "<b><blockquote expandable>›› ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>Pʏᴛʜᴏɴ 3</a> \n›› ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a> \n›› ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a></b></blockquote>",
    "REPLY": "<b>For More Join - @Hanime_Arena</b>",
    "SHORT_MSG": "<b>📊 ʜᴇʏ {first}, \n\n‼️ ɢᴇᴛ ᴀʟʟ ꜰɪʟᴇꜱ ɪɴ ᴀ ꜱɪɴɢʟᴇ ʟɪɴᴋ ‼️\n\n ⌯ ʏᴏᴜʀ ʟɪɴᴋ ɪꜱ ʀᴇᴀᴅʏ, ᴋɪɴᴅʟʏ ᴄʟɪᴄᴋ ᴏɴ ᴏᴘᴇɴ ʟɪɴᴋ ʙᴜᴛᴛᴏɴ..</b>",
    "START_PHOTO": "https://graph.org/file/510affa3d4b6c911c12e3.jpg",
    "FSUB_PHOTO": "https://telegra.ph/file/7a16ef7abae23bd238c82-b8fbdcb05422d71974.jpg",
    "SHORT_PIC": "https://telegra.ph/file/7a16ef7abae23bd238c82-b8fbdcb05422d71974.jpg",
    "SHORT": "https://telegra.ph/file/8aaf4df8c138c6685dcee-05d3b183d4978ec347.jpg",
    "TRIAL_USED": "<b>⚠️ {first}, aapne apna free trial ek baar use kar liya hai!</b>\n\nIs batch link se dobara file nahi milegi. Agar aur dekhna hai to niche premium le lo 👇"
}

def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
