from aiogram import types
from loader import dp, bot
from aiogram.dispatcher.filters import Text
from pytube import YouTube
from data.config import CHANNELS


@dp.message_handler(Text(startswith='http'))
async def youtubeVideoConverterAudio(message: types.Message):
    youtube_link = message.text
    from io import BytesIO
    buffer = BytesIO()
    url = YouTube(youtube_link)
    if url.check_availability() is None:
        audio = url.streams.get_audio_only()
        audio.stream_to_buffer(buffer=buffer)
        buffer.seek(0)
        video_title = url.title
        audio_file = await message.answer_audio(audio=buffer, caption=video_title)
        target_channel = CHANNELS[0]
        await audio_file.send_copy(chat_id=target_channel)
    else:
        await message.answer("Linkni qaytadan tekshirib ko'ring!")
