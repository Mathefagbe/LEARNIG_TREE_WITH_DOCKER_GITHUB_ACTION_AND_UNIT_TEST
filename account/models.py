from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.apps import apps
from django.contrib.auth.hashers import make_password

class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    #General method that create the user through password and email
    def _create_user(self,email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        email = GlobalUserModel.normalize_username(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    #when create user called email and password is passed
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)
    
    #when superuser is called email and password is passed
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)
    
class CustomUser(PermissionsMixin,AbstractBaseUser):
    email=models.EmailField(unique=True,null=False)
    first_name=models.CharField(max_length=200,null=True)
    last_name=models.CharField(max_length=20,null=True)

    EMAIL_FIELD = ""
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects=CustomUserManager()