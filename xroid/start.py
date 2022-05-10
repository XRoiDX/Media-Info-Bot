#XRoID


import os
import urllib
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from configs import Config
#from xroid.command import command Not Required

@Client.on_message(filters.command("start") & filters.private)
async def start(bot: Client, cmd: Message):
    await cmd.reply_text(
        f"""**Hello {cmd.from_user.mention}**

**I Am Most Powerful Media Info Bot.**

**Use Me To Generate Infomation Of Media Like Photo, Videos And Document.**

**I Also Work in Group**""",
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('➕ 𝑨𝒅𝒅 𝑴𝒆 𝑻𝒐 𝑼𝑹 𝑮𝒓𝒐𝒖𝒑 ➕', url=f'http://t.me/{Config.BOT_USERNAME}?startgroup=true')
            ],[
            InlineKeyboardButton('📢 𝑩𝒐𝒕𝒔 𝑪𝒉𝒂𝒏𝒏𝒆𝒍', url='https://t.me/XRoid_BotZ'),
            InlineKeyboardButton('💼 𝑺𝒖𝒑𝒑𝒐𝒓𝒕 𝑮𝒓𝒐𝒖𝒑', url=f'http://t.me/{Config.SUPPORT_GROUP}')
            ],[
            InlineKeyboardButton('🌐 𝑮𝒊𝒕𝒉𝒖𝒃 🌐', url='https://github.com/XRoiDX')
            ],[
            InlineKeyboardButton('⌦ Close The Menu ⌫', callback_data='close_data')
        ]]
        ),
     disable_web_page_preview=True
    )
