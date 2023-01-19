from django.shortcuts import render
from rest_framework import generics
from genricapp.serializers import UserSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .models import *
from rest_framework import mixins
# Create your views here.
class UserList(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserList1(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset().first()
        serializer = UserSerializer(queryset)
        return Response(serializer.data)

class UserDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
        