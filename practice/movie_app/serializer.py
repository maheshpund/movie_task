from rest_framework import serializers
from .models import Poster, Genre, Movie, User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['username','password','password']


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