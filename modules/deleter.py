import asyncio
from antigcast import Bot
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait, MessageDeleteForbidden, UserNotParticipant

from antigcast.config import *
from antigcast.helpers.tools import *
from antigcast.helpers.admins import *
from antigcast.helpers.message import *
from antigcast.helpers.database import *

# Tambahkan pengguna ke blacklist
@Bot.on_message(filters.command("ad") & ~filters.private & Admin)
async def addbluser(app: Bot, message: Message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id  # Ambil user ID dari pesan yang di-reply
        xxnx = await message.reply(f"`Menambahkan pengguna dengan ID {user_id} ke dalam blacklist...`")
        try:
            await add_bl_user(user_id)  # Fungsi untuk menambahkan user ke blacklist
        except BaseException as e:
            return await xxnx.edit(f"Error: `{e}`")

        try:
            await xxnx.edit(f"Pengguna dengan ID {user_id} `berhasil ditambahkan ke dalam blacklist.`")
        except:
            await app.send_message(message.chat.id, f"Pengguna dengan ID {user_id} `berhasil ditambahkan ke dalam blacklist.`")

        await asyncio.sleep(5)
        await xxnx.delete()
        await message.delete()
    else:
        await message.reply("Silakan reply pengguna yang ingin ditambahkan ke blacklist.")

# Hapus pengguna dari blacklist
@Bot.on_message(filters.command("rb") & ~filters.private & Admin)
async def delbluser(app: Bot, message: Message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id  # Ambil user ID dari pesan yang di-reply
        xxnx = await message.reply(f"`Menghapus pengguna dengan ID {user_id} dari blacklist...`")
        try:
            await remove_bl_user(user_id)  # Fungsi untuk menghapus user dari blacklist
        except BaseException as e:
            return await xxnx.edit(f"Error: `{e}`")

        try:
            await xxnx.edit(f"Pengguna dengan ID {user_id} `berhasil dihapus dari blacklist.`")
        except:
            await app.send_message(message.chat.id, f"Pengguna dengan ID {user_id} `berhasil dihapus dari blacklist.`")

        await asyncio.sleep(5)
        await xxnx.delete()
        await message.delete()
    else:
        await message.reply("Silakan reply pengguna yang ingin dihapus dari blacklist.")

# Periksa apakah pengguna ada di blacklist saat mengirim Gcast
@Bot.on_message(filters.text & ~filters.group)
async def deletermessag(app: Bot, message: Message):
    text = f"Maaf, Grup ini tidak terdaftar di dalam list. Silahkan hubungi owner untuk mendaftarkan Group Anda.\n\n**Bot akan meninggalkan grup!**"
    chat = message.chat.id
    chats = await get_actived_chats()
    
    if not await isGcast(filters, app, message):
        if chat not in chats:
            await message.reply(text=text)
            await asyncio.sleep(5)
            try:
                await app.leave_chat(chat)
            except UserNotParticipant as e:
                print(e)
            return
    
    try:
        if await isGcast(filters, app, message):
            # Cek apakah pengirim ada di blacklist
            if await is_user_blacklisted(message.from_user.id):  # Fungsi untuk memeriksa blacklist
                await message.reply("Anda tidak memiliki izin untuk mengirim Gcast.")
                await asyncio.sleep(5)
                await message.delete()
            else:
                await message.delete()
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await message.delete()
    except MessageDeleteForbidden:
        pass
