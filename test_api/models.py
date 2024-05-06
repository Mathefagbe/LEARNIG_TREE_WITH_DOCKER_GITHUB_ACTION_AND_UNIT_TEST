import re
from django.db import models
SPECIAL_CHARS_REGEX = "[^a-zA-Z0-9 \n\.]"


class Genre(models.Model):
    name=models.CharField(max_length=500)

class Artise(models.Model):
    def upload_to(instance, filename):
        url = re.sub(
            SPECIAL_CHARS_REGEX,
            "_",
            "images/artise/{filename}".format(filename=filename),
        )
        return url
    name=models.TextField()
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)
    bio=models.TextField()
    image=models.ImageField(upload_to=upload_to)

# Create your models here.
class Album(models.Model):
    def upload_to(instance, filename):
        url = re.sub(
            SPECIAL_CHARS_REGEX,
            "_",
            "images/track/{filename}".format(filename=filename),
        )
        return url
    artise=models.ForeignKey(Artise,on_delete=models.CASCADE)
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)
    name=models.TextField()
    release_year=models.DateField()
    cover_image=models.ImageField(upload_to=upload_to,null=True)


class Track(models.Model):
    def upload_to(instance, filename):
        url = re.sub(
            SPECIAL_CHARS_REGEX,
            "_",
            "images/track/{filename}".format(filename=filename),
        )
        return url
    artise=models.ForeignKey(Artise,on_delete=models.CASCADE,related_name="track_artise")
    album=models.ForeignKey(Album,on_delete=models.CASCADE,null=True)
    cover_image=models.ImageField(upload_to=upload_to,null=True)
    name=models.TextField()
    track_url=models.URLField()
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE,related_name="track_genre")
    year_release=models.DateField()
    created_at=models.DateField(auto_now_add=True)
    #duration



