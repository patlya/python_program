from django.urls import path,include
from genricapp.views import *
from genricapp import views
urlpatterns = [
    path('userlist1/', UserList.as_view(), name="userlist"),
    path('userlist1/<int:pk>/', UserList1.as_view(), name="userlist"),
    path('userdetail/<int:pk>/', UserDetail.as_view(), name="UserDetail")

]    