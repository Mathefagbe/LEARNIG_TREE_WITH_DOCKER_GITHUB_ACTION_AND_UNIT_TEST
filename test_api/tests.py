from django.test import TestCase
import pytest
from .models import Genre,Artise,Album,Track
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from account.models import CustomUser
from rest_framework.test import APITestCase

class GenreTest(APITestCase):
    def setUp(self):
        #create Genre
        self.user_data={
            "email":"fagbemi65@gmail.com",
            "first_name":"fagbemi",
            "last_name":"Joseph",
            "password":"test"
        }
        self.user=CustomUser.objects.create(**self.user_data)
        self.user.set_password(self.user_data['password'])
        self.user.save()
        self.url=reverse("genre")
        
        self.client.force_authenticate(user=self.user)
        self.data={
            "name":"hip hop"
        }
        Genre.objects.create(
            **self.data
            )

    #Create Genre has unauthorized user
    def test_create_genre_with_unauthenticated_user(self):
        self.client.logout()
        response=self.client.post(self.url,self.data,format="json")
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    #Create Genre has authorized User
    def test_create_genre_with_authenticated_user(self):
        response=self.client.post(self.url,self.data,format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_get_genre(self):
        response=self.client.get(self.url,format="json")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'],self.data['name'])
        self.assertEqual(len(response.data),1)

    def test_get_single_genre(self):
        self.single_gerne_url=reverse("single_genre",kwargs={"pk":1})
        response=self.client.get(self.single_gerne_url,format="json")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['name'],self.data['name'])

    def test_update_single_genre(self):
        self.single_gerne_url=reverse("single_genre",kwargs={"pk":1})
        new_data={
            "name":"Afrobeats"
        }
        response=self.client.put(self.single_gerne_url,new_data,format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertNotEqual(response.data['name'],self.data['name'])
        self.assertEqual(response.data['name'],new_data['name'])
 
        
        
        

class AlbumTest(TestCase):
    def setUp(self):
        pass

class ArtiseTest(TestCase):
    def setUp(self):
        pass

class TrackTest(TestCase):
    def setUp(self):
        pass