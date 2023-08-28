from django.db import models

# Create your models here.


class Movie_Post(models.Model):
    objects = None
    movie_name = models.CharField(max_length=20)
    movie_desc = models.TextField()
    movie_status = models.BooleanField(default=True)

    def __str__(self):
        return self. movie_name
    