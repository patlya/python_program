from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
# Create your models here.
from django.dispatch import receiver
class Album(models.Model):
    album_name = models.CharField(max_length=200, null=True, blank=True)
    artist = models.CharField(max_length=200, null=True, blank=True)

class Track(models.Model):
    order = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    duration = models.IntegerField(default=0)
    album = models.ForeignKey(Album , related_name='tracks',on_delete=models.CASCADE,null= True)

#this signals create auth token 
@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance = None , created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# class Location(models.Model):
#     name = models.CharField(max_length=100)
#     lon = models.FloatField()  # longitude
#     lat = models.FloatField()  # latitude

class Search(models.Model):
    address = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)