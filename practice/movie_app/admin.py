from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Movie, Genre, Poster, User


class Useradmin(UserAdmin):
    list_display = ['username','password']


class MovieAdmin(admin.ModelAdmin):
    list_display = ['movie_name','director','imdb_score','popularity']


class GenreAdmin(admin.ModelAdmin):
    list_display = ['movie','genre']


class PosterAdmin(admin.ModelAdmin):
    list_display = ['movie','poster']


admin.site.register(Movie,MovieAdmin)
admin.site.register(Genre,GenreAdmin)
admin.site.register(Poster,PosterAdmin)
admin.site.register(User,Useradmin)
