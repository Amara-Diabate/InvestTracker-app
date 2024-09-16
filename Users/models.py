from django.db import models
from django.conf import settings

class User(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
   

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
