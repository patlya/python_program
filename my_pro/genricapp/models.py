from django.db import models

# Create your models here.
class User(models.Model):
    PASS_OUT_YEAR = (
    ('2017','2017'),
    ('2018', '2018'),
    ('2019','2019'),
    ('2020','2020'),
    ('2021','2021'),
)
    name = models.CharField(max_length=200, null=True)
    passout = models.CharField(max_length=6, choices=PASS_OUT_YEAR, default='2021')

    def __str__(self):
        return self.name