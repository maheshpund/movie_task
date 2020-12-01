from django.db import models


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






