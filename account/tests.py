from django.test import TestCase
from .models import CustomUser
import pytest
from django.urls import reverse
from rest_framework import status
import json
from account.fixtures.user import user
from rest_framework.test import APITestCase
# Create your tests here.
# Create your tests here.
class UserModelTest(APITestCase):

    def setUp(self) -> None:
        #load initial data,this function hold the test all through the testing period
        self.user_data={
            "email":"fagbemi65@gmail.com",
            "first_name":"fagbemi",
            "last_name":"Joseph",
            "password":"test"
        }
        user=CustomUser.objects.create(**self.user_data)
        user.set_password(self.user_data['password'])
        user.save()
        self.url=reverse("signup")
        self.login_url=reverse("token_login")

    def test_user_registration(self):
        #create a data
        data={
            'email':'fagbemi@gmail.com',
	        'password':'testing',
	        'first_name':'john',
	        'last_name':'ben'
        }
        response=self.client.post(self.url,data,format="json")
        #do your check
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        user=CustomUser.objects.filter(email=data['email'])
        #since email is unique then i must have one user
        self.assertEqual(user.count(),1)


    def test_check_existing_email(self):
        #create a data
        data={
            'email':'fagbemi65@gmail.com',
	        'password':'testing',
	        'first_name':'john',
	        'last_name':'ben'
        }
        response=self.client.post(self.url,data,format="json")
        #do your check
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_check_first_name_required(self):
        #create a data
        data={
            'email':'fagbemi65@gmail.com',
	        'password':'testing',
	        'last_name':'ben'
        }
        response=self.client.post(self.url,data,format="json")
        #do your check
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)


    def test_user_login(self):
        data={
            "email":"fagbemi65@gmail.com",
            "password":"test"
        }
        response=self.client.post(self.login_url,data,format="json")
        
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        

    def test_user_invalid_login(self):
        data={
            "email":"fagbemi65@gmail.com",
            "password":"testing"
        }
        response=self.client.post(self.login_url,data,format="json")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)







       
