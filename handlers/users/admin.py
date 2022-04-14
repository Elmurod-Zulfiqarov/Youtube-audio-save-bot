import asyncio

from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot

@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
	users = db.select_all_users()
	print(users[0][0])
	await message.answer(users)

@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
	users = db.select_all_users()
	for user in users:
		user_id = user[0]
		text = "<b>❗️ Subscribe to @your_music_youtube channel</b>\n"
		text += f"<u>✅ All the music you are looking for is here! 🙂🙃😉</u>"

		await bot.send_message(chat_id=user_id, text=text)
		await asyncio.sleep(0.05)

@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
	db.delete_users()
	await message.answer("Clean Database!")

	