import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    await message.answer(f"<b> Salom👋👋👋, {message.from_user.full_name}!</b>\n"
                        f" <i>✅Men youtube videolarini audioga o'tkazib beruvchi 🤖Bot</i>\n"
                        f" <i>❗️Menga youtube video linkini yuboring!</i>")
    # Adminga xabar beramiz
    count = db.count_users()[0]
    if message.from_user.username:
        user_n = message.from_user.username
    else:
        user_n = 'username mavjudmas'
    msg = f"{message.from_user.full_name} va {user_n} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)
    