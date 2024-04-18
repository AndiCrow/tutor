from django.shortcuts import render

# Create your views here.
from .models import Music
from rest_framework import generics
from .serializers import MusicSerializer


# class MusicCreate(generics.CreateAPIView):
#     # This API is the endpoint to create new Music objects
#     queryset = Music.objects.all()
#     serializer_class = MusicSerializer

# class MusicList(generics.ListAPIView):
#     # This API is the endpoint to list Music objects
#     queryset = Music.objects.all()
#     serializer_class = MusicSerializer

# class MusicDelete(generics.DeleteAPIView):
#     # This API is the endpoint to delete Music objects
#     queryset = Music.objects.all()
#     serializer_class = MusicSerializer



class MusicCreateAPIView(generics.CreateAPIView):
    # This API is the endpoint to create new Music objects
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class MusicListAPIView(generics.ListAPIView):
    # This API is the endpoint to list Music objects
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class MusicDeleteAPIView(generics.DestroyAPIView):
    # This API is the endpoint to delete Music objects
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    