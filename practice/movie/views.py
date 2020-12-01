from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Movie
from .serializer import MovieSerializer
from rest_framework import filters, generics


class MovieView(generics.ListAPIView):
    """View for Movie ,search filter according to movie name"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['movie_name']
