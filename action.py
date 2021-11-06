# blogs ! 
from bot.scripts.one import *
from bot.Config import *
from pyrogram import filters 

@app.on_message(filters.command(["start"]))
async def startre():
  await start(bot, message)