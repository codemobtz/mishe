from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=120, unique=True)
    email = models.CharField(max_length=120, unique=True)
    phone_number = models.IntegerField(null=True, blank=True,verbose_name='Phone number')
    profile_picture = models.ImageField(null=True, blank=True) #TODO revisit after setting up static files
    

    def __str__(self):
        return self.username
