#Xroid

from datetime import datetime
from sys import version_info
from time import time
from configs import Config
from xroid.Duration import TimeFormatter
from pyrogram import Client, filters
from dkbotz.humanbytes import humanbytes
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

@Client.on_message((filters.video  | filters.audio | filters.document) & ~filters.channel)
async def help(client: Client, message: Message):
    if message.document:
       media = message.document
    if message.video:
       media = message.video
    if message.audio:
       media = message.audio
    if message.photo:
       media = message.photo

    text = ""
    if not message.photo:
        text = "**🗃️ File Details:**\n\n\n"
        text += f"📂 __File Name:__ `{media.file_name}`\n\n" if media.file_name else ""
        text += f"💽 __Mime Type:__ `{media.mime_type}`\n\n" if media.mime_type else ""
        text += f"📊 __File Size:__ `{humanbytes(media.file_size)}`\n\n" if media.file_size else ""
        if not message.document:
            text += f"🎞 __Duration:__ `{TimeFormatter(media.duration * 1000)}`\n\n" if media.duration else ""
            text += f"🔰 __Width:__ `{media.width}`\n\n" if media.width else ""
            text += f"⭕ __Height:__ `{media.height}`\n\n" if media.height else ""
            if message.audio:
                text += f"🎵 __Title:__ `{media.title}`\n\n" if media.title else ""
                text += f"🎙 __Performer:__ `{media.performer}`\n\n" if media.performer else ""
                if message.photo:
                    text += f"🔰 __Width:__ `{media.width}`\n\n" if media.width else ""
                    text += f"⭕ __Height:__ `{media.height}`\n\n" if media.height else ""
    text += f"__✏️ **Caption** : __ `{message.caption}`\n\n" if message.caption else ""
    text += f"**Generated By @{Config.BOT_USERNAME}**\n\n"

    await message.reply_text(text, quote=True)

