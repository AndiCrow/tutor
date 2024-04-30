from django.urls import path
from .views import MusicCreateAPIView, MusicDeleteAPIView, MusicListAPIView
from funapp import views

urlpatterns = [
    path('create/', MusicCreateAPIView.as_view(), name= 'createmusic'),
    path("", MusicListAPIView.as_view(), name ="list of music" ),
    path('delete/<int:pk>', MusicDeleteAPIView.as_view(), name="delete music"),
    path('music_create/', views.music_create, name="create music"),
   
]