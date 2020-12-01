from django.contrib import admin

from .models import Movie,Genre,Poster


class MovieAdmin(admin.ModelAdmin):
    list_display = ['movie_name','director','imdb_score','popularity']


class GenreAdmin(admin.ModelAdmin):
    list_display = ['movie','genre']


class PosterAdmin(admin.ModelAdmin):
    list_display = ['movie','poster']


admin.site.register(Movie,MovieAdmin)
admin.site.register(Genre,GenreAdmin)
admin.site.register(Poster,PosterAdmin)
