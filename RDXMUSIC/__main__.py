import asyncio, importlib
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall
import config
from RDXMUSIC import LOGGER, app, userbot
from RDXMUSIC.core.call import RDX
from RDXMUSIC.misc import sudo
from RDXMUSIC.plugins import ALL_MODULES
from RDXMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS
async def init():
    await sudo()
    try:
        for uid in await get_gbanned(): BANNED_USERS.add(uid)
        for uid in await get_banned_users(): BANNED_USERS.add(uid)
    except Exception as exc: LOGGER(__name__).warning("Ban lists not loaded: %s",exc)
    await app.start()
    for module in ALL_MODULES:
        try: importlib.import_module("RDXMUSIC.plugins"+module)
        except Exception as exc:
            LOGGER(__name__).exception("Plugin failed to load %s: %s",module,exc)
            raise
    LOGGER("RDXMUSIC.plugins").info("Reviewed plugins loaded successfully")
    await userbot.start(); await RDX.start()
    try: await RDX.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall: LOGGER("RDXMUSIC").warning("Logger voice chat inactive; continuing")
    except Exception as exc: LOGGER("RDXMUSIC").warning("Voice health check skipped: %s",exc)
    await RDX.decorators(); LOGGER("RDXMUSIC").info("RDX Music started successfully")
    await idle(); await app.stop(); await userbot.stop()
if __name__=="__main__": asyncio.run(init())
