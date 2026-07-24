import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
load_dotenv()

def required(name):
    value=getenv(name)
    if value is None or not value.strip():
        raise SystemExit(f"[CONFIG ERROR] Missing required variable: {name}")
    return value.strip()

def get_int(name, default=None, required_value=False):
    raw=required(name) if required_value else getenv(name)
    if raw is None or str(raw).strip()=="": return default
    try: return int(raw)
    except ValueError as e: raise SystemExit(f"[CONFIG ERROR] {name} must be numeric") from e

API_ID=get_int("API_ID", required_value=True)
API_HASH=required("API_HASH")
BOT_TOKEN=required("BOT_TOKEN")
MONGO_DB_URI=required("MONGO_DB_URI")
OWNER_ID=get_int("OWNER_ID", required_value=True)
LOGGER_ID=get_int("LOGGER_ID", required_value=True)
OWNER_USERNAME=getenv("OWNER_USERNAME","").strip().lstrip("@")
BOT_USERNAME=getenv("BOT_USERNAME","").strip().lstrip("@")
BOT_NAME=getenv("BOT_NAME","RDX Music").strip()
ASSUSERNAME=getenv("ASSUSERNAME","").strip().lstrip("@")
DURATION_LIMIT_MIN=get_int("DURATION_LIMIT",180)
PLAYLIST_FETCH_LIMIT=get_int("PLAYLIST_FETCH_LIMIT",25)
AUTO_LEAVING_ASSISTANT=getenv("AUTO_LEAVING_ASSISTANT","True")
AUTO_LEAVE_ASSISTANT_TIME=get_int("ASSISTANT_LEAVE_TIME",900)
SONG_DOWNLOAD_DURATION=get_int("SONG_DOWNLOAD_DURATION",180)
SONG_DOWNLOAD_DURATION_LIMIT=get_int("SONG_DOWNLOAD_DURATION_LIMIT",180)
TG_AUDIO_FILESIZE_LIMIT=get_int("TG_AUDIO_FILESIZE_LIMIT",2097152000)
TG_VIDEO_FILESIZE_LIMIT=get_int("TG_VIDEO_FILESIZE_LIMIT",2097152000)
STRING1=required("STRING_SESSION")
STRING2=getenv("STRING_SESSION2") or None
STRING3=getenv("STRING_SESSION3") or None
STRING4=getenv("STRING_SESSION4") or None
STRING5=getenv("STRING_SESSION5") or None
HEROKU_APP_NAME=getenv("HEROKU_APP_NAME")
HEROKU_API_KEY=getenv("HEROKU_API_KEY")
GIT_TOKEN=getenv("GIT_TOKEN")
UPSTREAM_REPO=getenv("UPSTREAM_REPO","https://github.com/RDX-RAj/RDXMUSIC")
UPSTREAM_BRANCH=getenv("UPSTREAM_BRANCH","Master")
SUPPORT_CHANNEL=getenv("SUPPORT_CHANNEL","").strip()
SUPPORT_CHAT=getenv("SUPPORT_CHAT","").strip()
SPOTIFY_CLIENT_ID=getenv("SPOTIFY_CLIENT_ID","").strip()
SPOTIFY_CLIENT_SECRET=getenv("SPOTIFY_CLIENT_SECRET","").strip()
BANNED_USERS=filters.user(); adminlist={}; lyrical={}; votemode={}; autoclean=[]; confirmer={}
START_IMG_URL=getenv("START_IMG_URL","https://telegra.ph/file/cfbdee8103102bcb2e5da.jpg")
PING_IMG_URL=getenv("PING_IMG_URL","https://telegra.ph/file/00360393a15daf7fc4e9d.jpg")
PLAYLIST_IMG_URL=getenv("PLAYLIST_IMG_URL","https://telegra.ph/file/d723f4c80da157fca1678.jpg")
STATS_IMG_URL=getenv("STATS_IMG_URL","https://telegra.ph/file/d30d11c4365c025c25e3e.jpg")
TELEGRAM_AUDIO_URL=getenv("TELEGRAM_AUDIO_URL","https://telegra.ph/file/48f39202823b358203234.jpg")
TELEGRAM_VIDEO_URL=getenv("TELEGRAM_VIDEO_URL","https://telegra.ph/file/e575ae40d6635250974e1.jpg")
STREAM_IMG_URL=getenv("STREAM_IMG_URL","https://telegra.ph/file/03efec694e41e891b29dc.jpg")
SOUNCLOUD_IMG_URL=getenv("SOUNCLOUD_IMG_URL",PLAYLIST_IMG_URL)
YOUTUBE_IMG_URL=getenv("YOUTUBE_IMG_URL","https://telegra.ph/file/4dc854f961cd3ce46899b.jpg")
SPOTIFY_ARTIST_IMG_URL=getenv("SPOTIFY_ARTIST_IMG_URL",PLAYLIST_IMG_URL)
SPOTIFY_ALBUM_IMG_URL=getenv("SPOTIFY_ALBUM_IMG_URL","https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg")
SPOTIFY_PLAYLIST_IMG_URL=getenv("SPOTIFY_PLAYLIST_IMG_URL",SPOTIFY_ALBUM_IMG_URL)
def time_to_seconds(value): return sum(int(x)*60**i for i,x in enumerate(reversed(str(value).split(":"))))
DURATION_LIMIT=time_to_seconds(f"{DURATION_LIMIT_MIN}:00")
for name,url in (("SUPPORT_CHANNEL",SUPPORT_CHANNEL),("SUPPORT_CHAT",SUPPORT_CHAT)):
    if url and not re.match(r"https?://",url): raise SystemExit(f"[CONFIG ERROR] {name} must begin with https://")
