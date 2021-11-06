import os 
import time 
from pyrogram import filters, client 
from config import SBot 


@SBot.on_message(filters.command("start"))
async def start(client, message):
  await client.send_message(
    message.chat.id,
    text="**I am alive!** \n **Please join my channel also !!!**",
    reply_markup=InlineKeyboardMarkup(
      [
        InlineKeyboardButton('Join Now', url="https://t.me/Animes_Encoded"
      ]
    )
  )
)

#@SBot.on_message(filters.command("id"))
#async def show_id(client, message):
 # await client.reply_text(
#    message.chat.id,
    #text=)
  
#@SBot.on_message(filters.incoming & (filters.video | filters.document))
#async def encode(client, cmd):
 # file_type = cmd.video or cmd.document
#  if not file_type.mime_type.startswith("video/"):
  #  await cmd.reply_text("This is not a video sarrrr.... Please go to school and learn something 🤭")
    return 
 # editable = await cmd.reply_text("Downloading Video ...", parse_mode="Markdown")
 # dl_loc = Config.DOWN_PATH + "/WatermarkAdder/" + str(cmd.from_user.id) + "/"
#  if not os.path.isdir(dl_loc):
 #   os.makedirs(dl_loc)
 # try:
  #  logs_msg = await bot.send_message(
   #   chat_id=-1001662056406,
     # text=f"Download Started!\n\n{user_info}", reply_to_message_id=forwarded_video.message_id,
    #  disable_web_page_preview=True,
    #  parse_mode="Markdown"
  #  )
  #  await asyncio.sleep(5)
  #  c_time = time.time()
  #  the_media = await bot.download_media(
    #  nessage=cmd,
    #  file_name=dl_loc,
   #   progress=progress_for_pyrogram,
     #progress_args=(
     #   "Downloading 👀....",
      #  editable,
      #  logs_msg,
       # c_time
     # )
  #  )
    
