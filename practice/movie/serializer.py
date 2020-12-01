from rest_framework import serializers
from .models import Poster, Genre, Movie


class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = ['id','poster']




class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre']


class MovieSerializer(serializers.ModelSerializer):
    poster = PosterSerializer(many=True)
    genres = GenreSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['movie_name','director','genres','imdb_score','popularity','poster']