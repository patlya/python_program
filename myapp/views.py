from django.shortcuts import render
# from rest_framework.exceptions import AllowAny, Throttled

# from mysite.account.throttle import UserLoginRateThrottle
# from mysite.myapp.serializers import UserCreateSerializer

# from .my_captcha import FormWithCaptcha
import requests


# # Create your views here.
# def home(request):
#     context={

#         "captcha":FormWithCaptcha,
#     }
#     return render(request,"home.html", context)

# class RegisterUserAPIView(CreateAPIView):

#     permission_classes = [AllowAny]
#     serializer_class = UserCreateSerializer
#     throttle_classes = (UserLoginRateThrottle,)

#     def perform_create(self, serializer):
#         user = serializer.save()

#     def throttled(self, request, wait):
#         raise Throttled(detail={
#             "message": "recaptcha_required",
#         })




# def get_ip():
#     response = requests.get('https://api64.ipify.org?format=json').json()
#     return response["ip"]


# def get_location():
#     ip_address = get_ip()
#     response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
#     location_data = {
#         "ip": ip_address,
#         "city": response.get("city"),
#         "region": response.get("region"),
#         "country": response.get("country_name")
#     }
#     return location_data


# print(get_location())

# ip = get('https://api.ipify.org').text
# print('My public IP address is: {}'.format(ip))


# import qrcode

# mydata="https://dev.inteer.org/#/login" 
# img = qrcode.make(mydata)
# img.save('MyQrCode.png')

# from requests import get
# ip=get("https://api.ipify.org").text
# print(ip)

# import socket
# hostname = socket.gethostname()
# ip_address = socket.gethostbyname(hostname)
# print(f"Hostname: {hostname}")
# print(f"IP Address: {ip_address}")

# import datetime
# from django.utils import timezone
# from .models import Email
# def add_foo():
#     # Create an instance of foo with expiration date now + one day
#     Email.objects.create(expiration_date=timezone.now() + datetime.timedelta(days=1))

from django.http import HttpResponse
from .helpers import *
from .my_captcha import *
from django.conf import settings
from django.core.mail import send_mail 

#celery -A myapp worker -l info -P eventlet "run celery on window use this typ of cmd "
def index(request):
    # sleepy.delay(60)
    send_mail_task.delay()
    # send_mail_without_celery()    
    return HttpResponse("<h1> done  <h1>")

def send_mail_fun():
    import pdb;pdb.set_trace()
    mailServer = smtplib.SMTP("smtp.gmail.com", 587, timeout=120)
    send_mail("CELERY WORKED PROPER", "CELERY IS COOL",
    'nagarharshita280@gmail.com',
    ["ranupatlya590@gmail.com"],
    fail_silently= False)
    return HttpResponse("<h1> Hello from  jdkjahdha <h1>")       