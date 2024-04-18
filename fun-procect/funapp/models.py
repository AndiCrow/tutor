from django.db import models

# Create your models here.


class Music(models.Model):
    name = models.CharField(max_length=250)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
