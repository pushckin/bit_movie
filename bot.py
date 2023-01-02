import os
import json

import requests

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.types import ParseMode
from aiogram.dispatcher import Dispatcher
from config import API_TOKEN, API_YOUTUBE

API_TOKEN = API_TOKEN
YOUTUBE_API_KEY = API_YOUTUBE

# For example use simple EchoBot
bot = Bot(token=API_TOKEN)

# For example use simple Storage for Dispatcher.
dp = Dispatcher(bot)


@dp.message_handler()
async def movie(message: types.Message):
    # Get movie title from the user
    movie_title = message.text.strip('/')
    if not movie_title:
        await message.reply("Please provide a movie title!")
        return

    # Send a request to the YouTube API
    api_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={movie_title}&type=video&key={YOUTUBE_API_KEY}"
    response = requests.get(api_url)
    video_data = response.json()

    # If the video was not found, reply with an error message
    if video_data['pageInfo']['totalResults'] == 0:
        await message.reply("Sorry, I couldn't find any videos matching your search.")
        return

    # Otherwise, get the first video from the search results and send its information to the user
    first_video = video_data['items'][0]
    video_title = first_video['snippet']['title']
    video_description = first_video['snippet']['description']
    video_url = f"https://www.youtube.com/watch?v={first_video['id']['videoId']}"

    video_info = f"*{video_title}*\n{video_description}\n{video_url}"

    await message.reply(video_info, parse_mode=ParseMode.MARKDOWN)


if __name__ == '__main__':
    executor.start_polling(dp)
