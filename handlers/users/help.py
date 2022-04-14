from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Commands: 🆘",
            "/start - Run the bot",
            "/help - Help",
            "/about - About Bot",
            "<a href='https://t.me/Elmurod_010409'>Admin - Contact</a>")
    
    await message.answer("\n".join(text))


@dp.message_handler(text="/about")
async def get_all_users(message: types.Message):
	await message.answer("👋 Welcome to YouTube Audio Save Bot🤖\n\n"
                "✅ Bot - YouTube videolarini audio shakliga aylantirib beradi\n"
                "🇺🇿YouTube 🎞video 🔗linkini botga yuboring - bot sizga 🎵audio formatini qaytarib yuboradi\n\n"
                "✅ Bot - Converts YouTube videos to audio format"
                "🇬🇧Send YouTube 🎞video 🔗 link to bot - bot will return 🎵audio format to you\n\n"
                "✅ Бот - конвертировать видео с YouTube в аудиоформат\n"
                "🇷🇺Отправьте боту ссылку на видео 🔗 YouTube - бот вернет вам 🎵аудио формат\n")

	