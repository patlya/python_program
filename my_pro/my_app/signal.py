from django.contrib.auth.signals import user_logged_in , user_logged_out, user_login_failed 
from django.contrib.auth.models import User
from my_app.views import hello
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete,pre_init, post_init
@receiver(user_logged_in, sender=User)
def login_success(sender, request,user, **kwargs):
    # print('-----------------------------')
    # print("log in signal")
    # print("sender", sender)
    # print("user",user)
    # print("Request",request)
    # print(f'kwargs:{kwargs}')
    hello(10)    
# user_logged_in.connect(login_success,sender=User) 
@receiver(pre_save, sender=User)
def pre_save(sender, instance, **kwargs):
    print("this run before model instance save")
