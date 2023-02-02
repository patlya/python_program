# from django.shortcuts import render
# from .models import *
# from .serialisers import *
# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
# # Create your views here.
# # Context are used in Django REST Framework when you want to add extra data to the serializer in addition to the object being serialized.
# class ImageViewSet(viewsets.ModelViewSet):
#     queryset = Image.objects.none()
#     serializer_class = ImageSerializer
#     permission_classes = (IsAuthenticated,)
#     http_method_names = ['post', ]

#     def get_serializer_context(self):
#         context = super(ImageViewSet, self).get_serializer_context()
#         context.update({"author": self.request.user})
#         context.update({"title": self.request.POST.get('title', None)})
#         return context

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)