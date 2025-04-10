from pyrogram import filters
from pyrogram.enums import ParseMode
from KuroAI import KuroAI as bot
from config import *
import asyncio
from KuroAI.KUROMAIN.DATABASE import auth_col, ban_col
from KuroAI import HANDLERS 




@bot.on_message(filters.command(["authorize", "auth"], prefixes=HANDLERS) & filters.user(OWNER_ID))
async def authorize_user(client, message):
    if not message.reply_to_message:
        msg = await message.reply(
        f"```shell\n[𝗞𝗨𝗥𝗢-𝗫𝗔𝗜] ==> Authorizing {user_id}...\n{bars[0]}```",
        parse_mode=ParseMode.MARKDOWN
    )

    for bar in bars[1:]:
        await asyncio.sleep(0.2)
        await msg.edit_text(f"```shell\n[𝗞𝗨𝗥𝗢-𝗫𝗔𝗜] ==> Authorizing {user_id}...\n{bar}```", parse_mode=ParseMode.MARKDOWN)

    auth_col.insert_one({"_id": user_id})
    await msg.edit_text(f"```shell\n[𝗞𝗨𝗥𝗢-𝗫𝗔𝗜] ==> {user_id} Authorized✅\n{bars[-1]}```", parse_mode=ParseMode.MARKDOWN)



    user = message.reply_to_message.from_user
    user_id = user.id

    if not auth_col.find_one({"_id": user_id}):
        return await message.reply("✅ This user is already authorized.")
    
    if ban_col.find_one({"_id": user_id}):
        return await message.reply("❌ This user is banned from using the bot.")

    bars = [
        "0%   [●◌◌◌◌◌◌◌◌◌]", "10%  [●◌◌◌◌◌◌◌◌◌]", "20%  [●●◌◌◌◌◌◌◌◌]",
        "30%  [●●●◌◌◌◌◌◌◌]", "40%  [●●●●◌◌◌◌◌◌]", "50%  [●●●●●◌◌◌◌◌]",
        "60%  [●●●●●●◌◌◌◌]", "70%  [●●●●●●●◌◌◌]", "80%  [●●●●●●●●◌◌]",
        "90%  [●●●●●●●●●◌]", "100% [●●●●●●●●●●]"
    ]


    await msg.reply("USER AUTHORIZED") 
    return 


