from django.db import models

from django.contrib.auth.models import AbstractBaseUser, UserManager,PermissionsMixin
from django.conf import settings

class CustomUserManager(UserManager):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def _str_(self,email,password):
        if not email:
            raise ValueError("Vous devez primordialement entrer une adresse email.")
        email = self.normalyze_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self,email=None,password=None):
        return self._create_user(email, password)
    
    def create_superuser(self,email, password):
        user = self._create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return self._create_superuser(email, password)
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True,default="",unique=True)
    first_nanme = models.CharField(max_length=225, blank=True, default="")
    last_name = models.CharField(max_length=550, blank=True, default="")
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(blank=True,null=True)

    objects= CustomUserManager()
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        return self.first_nanme
    
    def get_short_name(self):
        return self.first_nanme or self.email.split('@')[0]
    

        