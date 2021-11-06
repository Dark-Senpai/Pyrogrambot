import os
from pyrogram import Client

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
    # add api_id in config.py ( get from telegram.org )
    API_ID = get_config('API_ID')
    # add api_hash in config.py ( get from telegram.org)
    API_HASH = get_config('API_HASH')
    # array! add bot_token recieved from @botfather from telegram 
    BOT_TOKEN = get_config('BOT_TOKEN')
  except Exception as e:
    print(str(e))
    exit()
            
API_ID = 3281305
# ADD VALUE BELOW FOR API_HASH , DONT REMOVE " " 
API_HASH = "a9e62ec83fe3c22379e3e19195c8b3f6" 
# ADD VALUE BELOW FOR BOT_TOKEN , DONT REMOVE " " 
BOT_TOKEN = ""


SBot = Client(
  bot_token=BOT_TOKEN,
  api_id=API_ID,
  api_hash=API_HASH
)

# you guys can kang this 🤪
