from django.shortcuts import render
from django.http import HttpResponse
from .models import YoutubeData

# Create your views here.

def index(request):
    x = YoutubeData._meta.local_fields
    output = ', '.join([f.name for f in x])
    return HttpResponse(output)
