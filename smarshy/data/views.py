from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import YoutubeData
import json
import requests

# Create your views here.
def index(request):

    data = fetchVideos()

    # data = YoutubeMetadata.objects.all()
    response = []
    
    for i in data['items']:
        entry = {}
        # entry['title'] = i.title
        entry['title'] = i['snippet']['title']
        entry['description'] = i['snippet']['description']
        entry['publishedTimestamp'] = i['snippet']['publishedAt']
        entry['thumbnailUrl'] = i['snippet']['thumbnails']['default']['url']
        response.append(entry)
    
    res = json.dumps(response)
    return HttpResponse(res)

def fetchVideos():
    queryArguments = {
    'order':'date',
    'part':'snippet',
    'publishedAfter':'2020-04-04T15:51:12.000Z',
    'q':'mkbhd',
    'type':'video',
    'key':'AIzaSyDpzfHFfUJ8yzhzK93jwol8mp3kpKKEEMU'
    }
    url = 'https://content.googleapis.com/youtube/v3/search'
    r = requests.get(url,params=queryArguments)
    data = r.json()
    return data
