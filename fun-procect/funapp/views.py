from django.shortcuts import render, redirect

# Create your views here.
from .models import Music
from rest_framework import generics
from .serializers import MusicSerializer
from .forms import MusicForm


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

def music_create(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect(request, 'index.html' )
    else:
        form = MusicForm()
    return redirect(request, 'index.html')
