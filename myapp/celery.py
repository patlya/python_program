from celery import Celery
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
app = Celery('mysite')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

from celery.schedules import crontab
# from celery.task import periodic_task
from django.utils import timezone
from .models import *

# # @periodic_task(run_every=crontab(minute='*/5'))
# # def delete_old_foos():
# #     # Query all the foos in our database
# #     foos = Email.objects.all()

# #     # Iterate through them
# #     for foo in foos:

# #         # If the expiration date is bigger than now delete it
# #         if foo.expiration_date < timezone.now():
# #             foo.delete()
# #             # log deletion
# #     return "completed deleting foos at {}".format(timezone.now())

import datetime
from celery.schedules import crontab
# from celery.task import periodic_task
from django.utils import timezone

#     # import pdb;pdb.set_trace()
#     d = timezone.now() - datetime.timedelta(minutes=2)
#     #get expired orders
#     orders = Email.objects.filter(created_at__lt=d)
#     #delete them
#     orders.delete()