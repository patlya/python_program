from django.conf import settings
import requests

# def verify_recaptcha(g_token: str) -> bool:
#     data = {
#         'response': g_token,
#         'secret': settings.RE_CAPTCHA_SECRET_KEY

#     }
#     resp = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
#     result_json = resp.json()
#     return result_json.get('success') is True

from celery import shared_task
from time import sleep
from django.core.mail import send_mail
import smtplib

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_mail_task():
    # import pdb;pdb.set_trace()
    # subject = "CELERY WORKED PROPER"
    # message = "CELERY IS COOL"
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = ["ranupatlya590@gmail.com",]
    # send_mail(subject, message, email_from, recipient_list,fail_silently=True )
    request_link = settings.APP_CONST_URLS 
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("nagarharshita280@gmail.com", "eaietwlzqavrcghi")
    message = "this is mail sent to ranu by using celery............"
    subject = "mail send ......."
    msg_html ='<hi>hello ranu</h1>'+'Request Access Link:' + request_link
    s.sendmail("Notification Email For Organization","InterApp","nagarharshita280@gmail.com", "ranupatlya590@gmail.com",html_message=msg_html,fail_silently=True)
    print("ok")

