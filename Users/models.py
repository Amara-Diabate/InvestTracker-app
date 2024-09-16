from django.db import models

from django.contrib.auth.models import AbstractBaseUser, UserManager,PermissionsMixin
from django.conf import settings

class CustomUserManager(UserManager):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
   

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
