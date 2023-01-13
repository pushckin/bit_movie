from aiogram import Dispatcher, Bot, executor, types
from config import API_TOKEN, API_YOUTUBE
from pars import get_video_details, get_wilsa_details, reiting, wilsacom
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton



bot = Bot(API_TOKEN)
dp = Dispatcher(bot)



# конпка помощь
btn_help = KeyboardButton("В_рейтинге")
btn_wl = KeyboardButton('Wilsacom')
kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(btn_help).add(btn_wl)

# кнопки inline появляются в сообщение после нажатия кнопки помощь
video_buttens3 = []
for video in reiting:
    video_id = video['id']['videoId']
    video_title = video['snippet']['title']
    btn_3 = types.InlineKeyboardButton(text=video_title, callback_data=f'video_{video_id}')
    video_buttens3.append(btn_3)

video_buttens2 = []
for video_2 in wilsacom:
    video2_id = video_2['id']['videoId']
    video2_title = video_2['snippet']['title']
    btn_2 = types.InlineKeyboardButton(text=video2_title, callback_data=f'video2_{video2_id}')
    video_buttens2.append(btn_2)

markup = types.InlineKeyboardMarkup(row_width=1).add(*video_buttens3)
markup2 = types.InlineKeyboardMarkup(row_width=1).add(*video_buttens2)


# оброботчик команд команда start, в эту функцию встраевается кнопка помощь
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    # обработка кнопки помощь
    await bot.send_message(message.chat.id,"Привет! Нажмите на кнопку 'В рейтинге'",reply_markup=kb)

# оброботчики кнопок в inline режиме
@dp.message_handler(lambda message: message.text == "В_рейтинге")
async def show_inline_kb(message: types.Message):
    await bot.send_message(message.chat.id, "Привет! Выберите трейлер.", reply_markup=markup)

@dp.message_handler(lambda message: message.text == "Wilsacom")
async def show_inline_kb(message: types.Message):
    await bot.send_message(message.chat.id, "Привет! Выберите видео от Wilsocom.", reply_markup=markup2)




@dp.callback_query_handler(lambda c: c.data.startswith('video_'))
async def video_callback(callback_query: types.CallbackQuery):
    video_id = callback_query.data.split('_')[1]
    video_url = f'https://www.youtube.com/watch?v={video_id}'
    # get the video details using the video_id from the API
    video_details = get_video_details(video_id, API_YOUTUBE)
    # get the title and description of the video
    video_title = video_details['items'][0]['snippet']['title']
    message = f'Title: {video_title}\nLink: {video_url}'
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, message)

@dp.callback_query_handler(lambda c: c.data.startswith('video2_'))
async def video2_callback(callback_query: types.CallbackQuery):
    video2_id = callback_query.data.split('_')[1]
    video2_url = f'https://www.youtube.com/watch?v={video2_id}'
    video2_details = get_wilsa_details(video2_id, API_YOUTUBE)
    video2_title = video2_details['items'][0]['snippet']['title']
    message2 = f'Title: {video2_title}\nLink: {video2_url}'
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, message2)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)