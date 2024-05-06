from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CreateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=[
            "first_name",
            "last_name",
            "password",
            "email"
        ]
        extra_kwargs={
            "password":{
                "write_only":True
            },
            "first_name":{
                "required":True
            }
        }

    def create(self, validated_data):
        user=get_user_model().objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer): 

    """Override default token login to include user data"""

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        data.update(
            {
                "id": self.user.id,
                "email": self.user.email,
                "first_name": self.user.first_name,
                "last_name": self.user.last_name,
                "is_superuser": self.user.is_superuser,
                "is_staff": self.user.is_staff,
                "is_verified": self.user.is_verified
            }
        )

        return data