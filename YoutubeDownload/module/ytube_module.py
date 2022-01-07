from json import load
import threading
from bs4 import BeautifulSoup
import requests
from pytube import YouTube
import tkinter as tk
from datetime import datetime

def getUrls(url):
    index=url.find('channel/')
    r= url[index+len('channel/'):]
    YOUTUBE_API_KEY = "AIzaSyABlex8rGkfMcHNX0zrm4DOSIygWIWbsOE"
    youtube_channel_id = r

    youtube_spider = YoutubeSpider(YOUTUBE_API_KEY)
    uploads_id = youtube_spider.get_channel_uploads_id(youtube_channel_id)
    #print(uploads_id)

    video_ids = youtube_spider.get_playlist(uploads_id, max_results=5)
    
    #print(video_ids)
    list = []
    for video_id in video_ids:
        print("----------------------")
        video_info = youtube_spider.get_video(video_id)
        # print(video_info)
        list.append(video_info)
    return list
    #YOUTUBE_API_KEY = 'AIzaSyBCw4yUjzBeBESo9EptajtyjmSMM1jWm-A'

    #youtube = build('youtube','v3',developerKey=YOUTUBE_API_KEY)

    #search_response = youtube.search().list()

    # urls=[]
    # if '&list=' not in url:
    #     return urls
    # response = requests.get(url)
    # #response = youtube.search().list(part='id,snippet',type='video').execute()
    # if response.status_code != 200:
    #     print('error')
    #     return
    # bs= BeautifulSoup(response.text,'lxml')
    # aList = bs.find_all('a')
    # base = 'https://www.youtube.com/'
    # for a in aList:
    #     href = a.get('href')
    #     url = base + href
    #     if('&index='in url)and (url not in urls):
    #         urls.append(url)
    # return urls

lock = threading.Lock()
def startDownload(url,listbox):
    yt=YouTube(url)
    name = yt.title
    lock.acquire()
    no = listbox.size()
    listbox.insert(tk.END,f'{no:02d}:{name}.......Downloading')
    print('insert:',no,name)
    lock.release()

    yt.streams.first().download("D:\work\programming\Python\ProjuctYoutubeDownload")

    lock.acquire()
    print('update',no,name)
    listbox.delete(no)
    listbox.insert(no,f'{no:02d}:〇{name}.......Download Complete')
    lock.release()

class YoutubeSpider():
    def __init__(self, api_key):
        self.base_url = "https://www.googleapis.com/youtube/v3/"
        self.api_key = api_key

    def get_html_to_json(self, path):
        """組合 URL 後 GET 網頁並轉換成 JSON"""
        api_url = f"{self.base_url}{path}&key={self.api_key}"
        r = requests.get(api_url)
        if r.status_code == requests.codes.ok:
            data = r.json()
        else:
            data = None
        return data

    def get_channel_uploads_id(self, channel_id, part='contentDetails'):
        """取得頻道上傳影片清單的ID"""
        # UC7ia-A8gma8qcdC6GDcjwsQ
        path = f'channels?part={part}&id={channel_id}'
        data = self.get_html_to_json(path)
        try:
            uploads_id = data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        except KeyError:
            uploads_id = None
        return uploads_id

    def get_playlist(self, playlist_id, part='contentDetails', max_results=10):
        """取得影片清單ID中的影片"""
        # UU7ia-A8gma8qcdC6GDcjwsQ
        path = f'playlistItems?part={part}&playlistId={playlist_id}&maxResults={max_results}'
        data = self.get_html_to_json(path)
        if not data:
            return []

        video_ids = []
        for data_item in data['items']:
            video_ids.append(data_item['contentDetails']['videoId'])
        return video_ids

    def get_video(self, video_id, part='snippet,statistics'):
        """取得影片資訊"""
        # jyordOSr4cI
        # part = 'contentDetails,id,liveStreamingDetails,localizations,player,recordingDetails,snippet,statistics,status,topicDetails'
        path = f'videos?part={part}&id={video_id}'
        data = self.get_html_to_json(path)
        if not data:
            return {}
        # 以下整理並提取需要的資料
        data_item = data['items'][0]

        try:
            # 2019-09-29T04:17:05Z
            time_ = datetime.strptime(data_item['snippet']['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
        except ValueError:
            # 日期格式錯誤
            time_ = None

        url_ = "https://www.youtube.com/watch?v="+data_item['id']

        info = {
            'id': data_item['id'],
            'channelTitle': data_item['snippet']['channelTitle'],
            'publishedAt': time_,
            'video_url': url_,
            'title': data_item['snippet']['title'],
            'description': data_item['snippet']['description'],
            'likeCount': data_item['statistics']['likeCount'],
            # 'dislikeCount': data_item['statistics']['dislikeCount'],
            'commentCount': data_item['statistics']['commentCount'],
            'viewCount': data_item['statistics']['viewCount']
        }
        return url_