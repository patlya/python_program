from django.db import models

# Create your models here.
class Track(models.Model):
    order = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    duration = models.IntegerField(default=0)

class Album(models.Model):
    album_name = models.CharField(max_length=200, null=True, blank=True)
    artist = models.CharField(max_length=200, null=True, blank=True)
