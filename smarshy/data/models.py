from django.db import models

# Create your models here.
class YoutubeData(models.Model):
    video_title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    timestamp = models.DateTimeField('Publishing date')
    pic_url = models.CharField(max_length=200)
