from django.db import models

class job(models.Model):
    moviePoster = models.ImageField(upload_to = 'images/')
    movieDescription = models.CharField(max_length=200)

# Create your models here.
