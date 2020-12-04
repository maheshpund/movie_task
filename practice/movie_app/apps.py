from django.apps import AppConfig

class MovieConfig(AppConfig):
    name = 'movie_app'

    def ready(self):
        import movie_app.signals
