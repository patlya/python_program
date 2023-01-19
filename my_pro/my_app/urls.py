
from django.urls import path,include
from my_app.views import *
from rest_framework.authtoken import views
from my_app import views as map_view
# # from rest_framework.routers import DefaultRouter

# # router = DefaultRouter()
# # router.register('Album',Albumlist)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
#     # path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('album',Albumlist.as_view(), name="album"),
    path('album/<int:pk>/',Albumlist1.as_view(), name="album"),
    path('examview',ExampleView.as_view(), name="userview"),
    path('list/', Albumlist2.as_view(), name = 'Albumlist2'),
    path('list1/', Albumlist3.as_view(), name = 'Albumlist2'),
    path('indexpage/', map_view.indexpage, name = 'asd'),
    path('page/', paginatorRecordsView.as_view(), name="page"),
    # path('send_mail/',send_mail_fun(),name='get_loc'),
    path('albumlist/', AlbumListView.as_view(), name='albumlist')
    
]
