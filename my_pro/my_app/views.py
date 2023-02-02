from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import io
from rest_framework.parsers import JSONParser

from rest_framework.authentication import TokenAuthentication, BasicAuthentication,SessionAuthentication 
from django.contrib.auth.models import User 
from rest_framework.permissions import IsAuthenticated , IsAdminUser ,IsAuthenticatedOrReadOnly, AllowAny, DjangoModelPermissions
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle ,ScopedRateThrottle
from rest_framework.views import APIView
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
import folium
import geocoder
from django.shortcuts import render , redirect
from .forms import SearchForm
from django.http import HttpResponse
from django.core.mail import send_mail     
from django.views.generic import ListView
# Create your views here.


factory = APIRequestFactory()
request = factory.get('/')


for user in User.objects.all():
    token = Token.objects.get_or_create(user=user)
    print(token)

class Albumlist(APIView):
    """
    authentication_classes = [BasicAuthentication]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser] 
    permission_classes = [IsAuthenticatedOrReadOnly] 
    DjangoModelPermissions me hme admin se permision deni pdti he jisse vo add , delete , update sb kr skta he 
    permission_classes = [DjangoModelPermissions] 

    ##we generate token using this cmd :- python manage.py drf_create_token admin
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class Albumlist1(APIView):
    def get(self, request):
        track = Track.objects.all()
        # serializer = TrackSerializer1(instance=album, many=True)
        serializer = Trackserializer(instance=track)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        data= request.data
        # import pdb;pdb.set_trace()
        serializer = TrackSerializer1(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class Albumlist(APIView):    
    # def get(self, request):
    #     import pdb;pdb.set_trace()
    #     album = Album.objects.all()
    #     serializer = AlbumSerializer(instance=album, many=True)
    #     # track = Track.objects.all()
    #     # serializer = Trackserializer(instance=track, many=True)
    #     return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    '''
    using query_pramas data in get method
    '''
    def get(self, request):
        album_id= request.query_params.get('album')
        artist= request.query_params.get('artist')
        if artist != None and album_id !=None:
            album = Album.objects.filter(id=album_id,artist=artist)
            serializer = AlbumSerializernew(instance=album, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"data not found"},status=status.HTTP_404_NOT_FOUND)    

    def post(self, request):
        data= request.data
        import pdb;pdb.set_trace()
        album_id= request.query_params.get('album')
        artist= request.query_params.get('artist')
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)
        return Response(serializer.errors)
    '''
    using query_pramas data use in Post method but django rules we should't user query params with Post
    '''

    # def post(self, request):
    #     data= request.data
    #     import pdb;pdb.set_trace()
    #     album_id= request.query_params.get('album')
    #     artist= request.query_params.get('artist')
    #     serializer = AlbumSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save() 
    #     if artist != None and album_id !=None:
    #         album = Album.objects.filter(id=album_id,artist=artist)
    #         serializer = AlbumSerializernew(instance=album, many=True)
    #         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    #     return Response({"data not found"},status=status.HTTP_404_NOT_FOUND)           
# ..............................................................
'''
not understand context 
$ Context are used in Django REST Framework when you want to add extra data to the serializer in addition to the object being serialized.
'''
class Albumlistnew(APIView): 
     
    def get(self, request):
        album = Album.objects.all()

        serializer = AlbumSerializernew(instance=album, many=True)
        # track = Track.objects.all()
        # serializer = Trackserializer(instance=track, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


# CRUD START HERE..............................
class Crud_by_id(APIView):
    def get_note(self, id):
        try:
            return Album.objects.get(id=id)
        except:
            return None

    def get(self, request, id):
        note = self.get_note(id=id)
        if note == None:
            return Response("id not available", status=status.HTTP_404_NOT_FOUND) 
        serializer = AlbumSerializer(note)
        return Response({"status": "success", "note": serializer.data})   

    def patch(self,request, id):
        note = self.get_note(id=id) 
        serializer = AlbumSerializer(note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "update success", "note": serializer.data})    

    def delete(self , request, id):
        import pdb;pdb.set_trace()
        note = self.get_note(id=id)
        if not note:
            return Response("id not available",status=status.HTTP_404_NOT_FOUND)
        note.delete()
        return Response("delete success")


#throtling ---------------------------------------------

class ExampleView(APIView):
    throttle_classes = [UserRateThrottle, ScopedRateThrottle]
    throttle_scope = 'contacts'

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)

# filter --------------------------------
from rest_framework import filters
class Albumlist2(generics.ListAPIView):
    serializer_class = AlbumSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['album_name']
    def get_queryset(self): 
        data  = Album.objects.all()
        return data  

class Albumlist3(generics.ListAPIView):     
    #search-------------------------
    queryset  = Album.objects.all()  
    serializer_class = AlbumSerializer
    filter_backends = [filters.SearchFilter]
    # search_fields = ['artist']
    search_fields = ['album_name']

# map ----------------------------
def indexpage(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asd')
    else:
        form = SearchForm()    
    address  =  Search.objects.all().last()
    # import pdb;pdb.set_trace()
    location = geocoder.osm(address.address)
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat == None or lng == None:
        address.delete()
        return HttpResponse("your address input invalid")
    m = folium.Map(location=[19, -12], zoom_start=6)
    # folium.Marker([22.7196, 75.8577], tooltip='clicke for more', popup='india').add_to(m)
    folium.Marker([lat , lng], tooltip='clicke for more', popup=country).add_to(m)
    m = m._repr_html_()
    context ={
        'm':m,
        'form':form,
    }
    return render(request, 'index.html', context)   

#pagination---------------------------------------------
from rest_framework.pagination import LimitOffsetPagination ,PageNumberPagination, CursorPagination
class LargeResultsSetPagination(CursorPagination):
    '''
    CursorPagination me ek error milti he vo timestamp create krne ka bolta he but esa nhi krte to hm ordeering ka use kr ke kr lete 
    or esme count nhi aata he 
    '''
    page_size = 1
    ordering = 'album_name'
    
class paginatorRecordsView(generics.ListAPIView):
    # queryset = Album.objects.all()
    queryset = Track.objects.all()
    # serializer_class = AlbumSerializer
    serializer_class = TrackSerializer
    pagination_class = LargeResultsSetPagination 

def hello(self):
    x = 10+20
    return print(x) 

def send_mail_fun(request):
    # import pdb;pdb.set_trace()
    send_mail("CELERY WORKED PROPER", "CELERY IS COOL",
    'nagarharshita280@gmail.com',
    ["ranupatlya590@gmail.com"],
    fail_silently= False)

        
class AlbumListView(ListView):
    model = Album