from django.db import models

# Create your models here.
from datetime import timedelta
# from django.db import models
from django.utils.timezone import now

# class Track(models.Model):
#     order = models.CharField(max_length=200, null=True, blank=True)
#     title = models.CharField(max_length=200, null=True, blank=True)
#     duration = models.IntegerField(default=0)

# class Album(models.Model):
#     album_name = models.CharField(max_length=200, null=True, blank=True)
#     artist = models.CharField(max_length=200, null=True, blank=True)

# class Email(models.Model):
#     email = models.EmailField(max_length=256)
#     created_at = models.DateTimeField(auto_now_add=True)

#     # def __str__(self):
#     #     return 'code: ' + str(self.code)

#     @property
#     def deletes_in_ten_seconds(self):
#         time = self.created_at + timedelta(seconds=10)
#         query = Email.objects.get(pk=self.pk)
#         if time > now():
#             query.delete()