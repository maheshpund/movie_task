from django.urls import path

from . import views

urlpatterns=[
    path('',views.MovieView.as_view()),
    path('user/',views.UserView.as_view())
]