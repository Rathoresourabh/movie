from django.db import models

# Create your models here.
class blogs (models.Model):
    Title = models.CharField(max_length=100)
    Publication_Date = models.DateTimeField()
    Body = models.TextField(max_length=500)
    Image = models.ImageField(upload_to = 'images/')
