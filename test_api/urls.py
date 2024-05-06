from django.contrib import admin
from django.urls import path
from .views import (
    TrackApiView,
    SingleTrackApiView,
    GenreApiView,
    SingleGenreApiView
)

urlpatterns = [
    path("track/",TrackApiView.as_view(),name="track"),
    path("track/<int:pk>/",SingleTrackApiView.as_view(),name="singe_track"),
    path("genre/",GenreApiView.as_view(),name="genre"),
    path("genre/<int:pk>/",SingleGenreApiView.as_view(),name="single_genre")
]