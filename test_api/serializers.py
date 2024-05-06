from .models import *
from rest_framework import serializers


class GenreSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields="__all__"

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model=Album
        fields="__all__"

class ArtiseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Artise
        fields="__all__"

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Track
        fields="__all__"