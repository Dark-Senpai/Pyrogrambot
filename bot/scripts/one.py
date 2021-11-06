# the following codes contain spoilers 😂
from pyrogram import filters 
from bot.Config import *

@app.on_message(filters.command(["start"]))
async def start(bot, message):
  await bot.send_message(
    message.chat.id,
    text="**Hi! I am online. Join my channel**!",
    reply_markup=InlineKeyboardMarkup(
      [InlineKeyboardButton("CHANNEL", url="https://t.me/Animes_Encoded")],
    ),
  )

