from aiogram import Dispatcher, Bot, executor, types
from config import API_TOKEN, API_YOUTUBE
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
# from pars import *
import json
import requests

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)



vReiteng_id = 'UClmI-b4_ro8UJLaNbiS9Isw'

# Функция, которая возвращает список видео с канала
def get_videos_from_channel(vReiteng_id, API_YOUTUBE):
    url = f'https://www.googleapis.com/youtube/v3/search?key={API_YOUTUBE}&channelId={vReiteng_id}&part=snippet,id&order=date&maxResults=5'
    response = requests.get(url)
    reiting = response.json()['items']
    return reiting

# конпка помощь
btn_help = KeyboardButton("В_рейтинге")
kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(btn_help)

# кнопки inline появляются в сообщение после нажатия кнопки помощь
reiting = get_videos_from_channel(vReiteng_id, API_YOUTUBE)
markup = types.InlineKeyboardMarkup(row_width=2)

video_buttens3 = []
for video in reiting:
    video_id = video['id']['videoId']
    video_title = video['snippet']['title']
    btn_3 = types.InlineKeyboardButton(text=video_title, callback_data=f'video_{video_id}')
    video_buttens3.append(btn_3)

markup.add(*video_buttens3)

# оброботчик команд команда start, в эту функцию встраевается кнопка помощь
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    # обработка кнопки помощь
    await bot.send_message(message.chat.id,"Привет! Нажмите на кнопку 'В рейтинге'",reply_markup=kb)

# оброботчики кнопок в inline режиме
@dp.message_handler(lambda message: message.text == "В_рейтинге")
async def show_inline_kb(message: types.Message):
    await bot.send_message(message.chat.id, "Привет! Выберите трейлер.", reply_markup=markup)



def get_video_details(video_id, API_YOUTUBE):
    url = f'https://www.googleapis.com/youtube/v3/videos?key={API_YOUTUBE}&id={video_id}&part=snippet,contentDetails,statistics'
    response = requests.get(url)
    return response.json()

@dp.callback_query_handler(lambda c: c.data.startswith('video_'))
async def video_callback(callback_query: types.CallbackQuery):
    video_id = callback_query.data.split('_')[1]
    video_url = f'https://www.youtube.com/watch?v={video_id}'
    # get the video details using the video_id from the API
    video_details = get_video_details(video_id, API_YOUTUBE)
    # get the title and description of the video
    video_title = video_details['items'][0]['snippet']['title']
    # video_description = video_details['items'][0]['snippet']['description']
    message = f'Title: {video_title}\nLink: {video_url}'
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, message)

# with open("videos.json", "w") as file:
#     json.dump(reiting, file, indent=2)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)