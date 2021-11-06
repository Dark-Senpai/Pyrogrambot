# the following codes contain spoilers 😂
async def start(bot, message):
  await bot.send_message(
    message.chat.id,
    text="**Hi! I am online. Join my channel**!",
    reply_markup=InlineKeyboardMarkup(
      [InlineKeyboardButton("CHANNEL", url="https://t.me/Animes_Encoded")],
    ),
  )
