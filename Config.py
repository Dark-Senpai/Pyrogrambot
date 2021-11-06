import os
import logging
from pyrogram import Client 

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
def get_config(name: str, d_v=None, should_prompt=False):
  val = os.environ.get(name, d_v)
  if not val and should_prompt:
    try:
      val = input(f"enter {name}'s value: ")
    except EOFError:
      val = d_v
      print("\n")
  return val 

class vars(object):
  try:
    API_ID = get_config('API_ID')
    API_HASH = get_config('API_HASH')
    BOT_TOKEN = get_config('BOT_TOKEN')
  except Exception as e:
    print(str(e))
    exit()
    
API_ID = 16067877
API_HASH = "5f18154b89b1792829d1c7b1e1dd7e82"
BOT_TOKEN = "2124586685:AAEtpsQEurB2-rfJan7kzyrrPJvRtl0aPGo" 

app = Client(
  "Anime",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN
)

app.run()
