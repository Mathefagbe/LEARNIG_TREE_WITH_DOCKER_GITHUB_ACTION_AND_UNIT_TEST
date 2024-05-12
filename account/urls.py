from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib import admin
from django.urls import path
from .views import (
 RegisterAPiView,
 LoginView,
 CustomTokenObtainPairViewSet,
 TestCeleryApiView
)

urlpatterns = [
    path("token/login/",LoginView.as_view(),name="token_login"),
    path("signup/",RegisterAPiView.as_view(),
         name="signup"),

    path("test/",TestCeleryApiView.as_view())
]