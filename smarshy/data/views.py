from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import YoutubeData
import json
import requests
import dateutil.parser

# Create your views here.
def index(request):

    data = fetchVideos()

    response = []
    
    for i in data['items']:
        entry = {}
        # entry['avds'] = str(i.publishTimestamp)
        entry['video_title'] = i['snippet']['title']
        entry['desc'] = i['snippet']['description']
        entry['timestamp'] = str(i['snippet']['publishedAt'])
        entry['pic_url'] = i['snippet']['thumbnails']['default']['url']
        response.append(entry)

        dbRow = YoutubeData()
        dbRow.video_title = entry['video_title']
        dbRow.desc = entry['desc']
        dbRow.timestamp = str(dateutil.parser.parse(entry['timestamp']))
        dbRow.pic_url = entry['pic_url']
        dbRow.save()
    
    res = json.dumps(response, indent=4, sort_keys=True)
    return HttpResponse(res)

def fetchVideos():
    queryArguments = {
    'order':'date',
    'part':'snippet',
    'maxResults': 5,
    'publishedAfter':'2000-04-04T15:51:12.000Z',
    'q':'coronavirus',
    'type':'video',
    'key':'AIzaSyDpzfHFfUJ8yzhzK93jwol8mp3kpKKEEMU'
    }
    url = 'https://content.googleapis.com/youtube/v3/search'
    r = requests.get(url,params=queryArguments)
    data = r.json()
    return data
