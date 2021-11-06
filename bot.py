from pyrogram import filters 
from Config import *
  
@app.on_message(filters.command(["start"]))
async def start(bot, message):
  await bot.send_message(
    message.chat.id,
    text="**Hi! I am online. Click the below button to know my master**!",
    reply_markup=InlineKeyboardMarkup(
      [InlineKeyboardButton('BOSS', url="https://t.me/Parth_Senpai")],
    ),
  )
