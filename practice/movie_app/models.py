from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=150,unique=True)

    def __str__(self):
        return self.username

    class Meta:
        permissions = (
                       ("movie_app_movie", "can view movie"),
                      )


class Movie(models.Model):
    movie_name = models.CharField(max_length=20)
    director = models.CharField(max_length=20)
    imdb_score = models.FloatField()
    popularity = models.FloatField()

    def __str__(self):
        return self.movie_name


class Genre(models.Model):
    movie = models.ForeignKey(Movie,related_name='genres',on_delete=models.CASCADE)
    genre = models.CharField(max_length=20)


class Poster(models.Model):
    movie = models.ForeignKey(Movie,related_name='poster',on_delete=models.CASCADE)
    poster = models.ImageField(upload_to='poster')






