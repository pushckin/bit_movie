from config import API_YOUTUBE
import json
import requests

vReiteng_id = 'UClmI-b4_ro8UJLaNbiS9Isw'

# Функция, которая возвращает список видео с канала
def get_videos_from_channel(vReiteng_id, API_YOUTUBE):
    url = f'https://www.googleapis.com/youtube/v3/search?key={API_YOUTUBE}&channelId={vReiteng_id}&part=snippet,id&order=date&maxResults=5'
    response = requests.get(url)
    reiting = response.json()['items']
    return reiting


# Используя функцию, мы можем получить список видео и создать кнопки Inline
# для каждого видео с названием видео и идентификатором callback_data,
# соответствующим идентификатору видео

reiting = get_videos_from_channel(vReiteng_id, API_YOUTUBE)
# with open("videos.json", "w") as file:
#     json.dump(videos, file, indent=2)
# markup = InlineKeyboardMarkup()
# for video in reiting:
#     video_id = video['id']['videoId']
#     video_title = video['snippet']['title']
#     button = InlineKeyboardButton(text=video_title, callback_data=f'video_{video_id}')
#     markup.add(button)



# async def show_inline_kb(message: types.Message):
#     reiting = get_videos_from_channel(vReiteng_id, API_YOUTUBE)
#     markup = types.InlineKeyboardMarkup(row_width=2)
#
#     btn = types.InlineKeyboardButton("кнопка1", callback_data="bt")
#     btn_2 = types.InlineKeyboardButton("кнопка2", callback_data="bt 2")
#     for video in reiting:
#         video_id = video['id']['videoId']
#         video_title = video['snippet']['title']
#         btn_3 = types.InlineKeyboardButton(text=video_title, callback_data=f'video_{video_id}')
#     btn_4 = types.InlineKeyboardButton("кнопка4", callback_data="bt 4")
#     markup.add(btn).add(btn_2).add(btn_3).add(btn_4)
#     await bot.send_message(message.chat.id, "Привет! Нажми на лубую кнопку, чтобы начать.", reply_markup=markup)