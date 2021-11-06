import os
import logging
import pyrogram
from decouple import config

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

try:
  APP_ID = config("API_ID", default=None, cast=int)
  API_HASH = config("API_HASH", default=None)
  BOT_TOKEN = config("BOT_TOKEN", default=None)
except Exception as e:
  print("Hey kid, vars are missing 🤭, leanr some coding and try again 😂")
  print(str(e))
  exit()
  

plugins = dict(root="bot/scripts")
app = pyrogram.Client(
  "Anime",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN,
  plugins=plugins
)

app.run()
