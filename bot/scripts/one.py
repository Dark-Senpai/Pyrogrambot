from pyrogram import Client, filters

@Client.on_message(filters.command(["start"]))
async def start(bot, message):
  await bot.send_message(
    message.chat.id,
    text="**Hi! I am online. Join my channel**!",
    reply_markup=InlineKeyboardMarkup(
      [InlineKeyboardButton("CHANNEL", url="https://t.me/Animes_Encoded"]),
    ),
  )
