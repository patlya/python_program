from django.urls import path
from .views import *

urlpatterns =[

    # path("",views.home, name='home'),
    # path('register/', views.RegisterUserAPIView.as_view(), name='throw'),
    # path('gets/',views.get_ip,name="gets"),
    path('send_mail/',send_mail_fun(),name='get_loc'),
    path('',index,name='index'),

]