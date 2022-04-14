from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Commands: 🆘",
            "/start - Run the bot",
            "/help - Help",
            "/about - About Bot",
            "/video - <a href='https://t.me/Youtube_video_savebot'>YouTube Video Save Bot</a>",
            "Contact - <a href='https://t.me/Elmurod_010409'>Admin</a>")
    
    await message.answer("\n".join(text))


@dp.message_handler(text="/about")
async def about_audio_bot(message: types.Message):
	await message.answer("👋 Welcome to YouTube Audio Save Bot🤖\n\n"
                "✅ Bot - YouTube videolarini audio shakliga aylantirib beradi\n"
                "🇺🇿YouTube 🎞video 🔗linkini botga yuboring - bot sizga 🎵audio formatini qaytarib yuboradi\n\n"
                "✅ Bot - Converts YouTube videos to audio format\n"
                "🇬🇧Send YouTube 🎞video 🔗 link to bot - bot will return 🎵audio format to you\n\n"
                "✅ Бот - конвертировать видео с YouTube в аудиоформат\n"
                "🇷🇺Отправьте боту ссылку на видео 🔗 YouTube - бот вернет вам 🎵аудио формат\n")



@dp.message_handler(text="/video")
async def video_bot(message: types.Message):
	text = "<b>❗️ Subscribe to @your_music_youtube channel</b>\n"
	text += f"<u>✅ All the music you are looking for is here! 🙂🙃😉</u>\n"
	text += f"<b>Use the <a href='https://t.me/video_to_audio_converterbot'>YouTube Audio Save Bot</a> @video_to_audio_converterbot</b>\n"
	text += f"<b>Use the <a href='https://t.me/Youtube_video_savebot'>YouTube Video Save Bot</a> @Youtube_video_savebot</b>\n"

	await message.answer(text)	