import json
import requests
from config import API_YOUTUBE



vReiteng_id = 'UClmI-b4_ro8UJLaNbiS9Isw'
wilsa_id = 'UCt7sv-NKh44rHAEb-qCCxvA'

# Функция, которая возвращает список видео с канала
def get_videos_from_channel(vReiteng_id, API_YOUTUBE):
    url = f'https://www.googleapis.com/youtube/v3/search?key={API_YOUTUBE}&channelId={vReiteng_id}&part=snippet,id&order=date&maxResults=5'
    response = requests.get(url)
    reiting = response.json()['items']
    return reiting
reiting = get_videos_from_channel(vReiteng_id, API_YOUTUBE)

def get_video_wilacom(wilsa_id, API_YOUTUBE):
    url = f'https://www.googleapis.com/youtube/v3/search?key={API_YOUTUBE}&channelId={wilsa_id}&part=snippet,id&order=date&maxResults=5'
    response = requests.get(url)
    wilsacom = response.json()['items']
    return wilsacom
wilsacom = get_video_wilacom(wilsa_id, API_YOUTUBE)

def get_video_details(video_id, API_YOUTUBE):
    url = f'https://www.googleapis.com/youtube/v3/videos?key={API_YOUTUBE}&id={video_id}&part=snippet,contentDetails,statistics'
    response = requests.get(url)
    return response.json()

def get_wilsa_details(video2_id, API_YOUTUBE):
    url = f'https://www.googleapis.com/youtube/v3/videos?key={API_YOUTUBE}&id={video2_id}&part=snippet,contentDetails,statistics'
    responseWilsa = requests.get(url)
    return responseWilsa.json()

