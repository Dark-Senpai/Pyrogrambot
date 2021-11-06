# blogs ! 
from bot.scripts.one import *
from bot.Config import *
from pyrogram import Client, filters 


@Client.on_message(filters.command(["start"]))
await start(bot, message)


  

