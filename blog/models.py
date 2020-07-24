from django.db import models

# Create your models here.
class Blog (models.Model):
    movieName = models.CharField(max_length=100)
    createdDate = models.DateTimeField()
   
    movieDescription = models.TextField(max_length=500)
    moviePoster = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.movieName

    def summary(self):
        return self.movieDescription[:100]

    def createdDate_pretty(self):
        return self.createdDate.strftime('%b %e %Y')

    