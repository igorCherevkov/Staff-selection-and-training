from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(primary_key=True, db_index=True)
    image = models.ImageField(upload_to='users_images', blank=True, null=True)    
    profession = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(blank=True, null=True, default=None)
    age = models.IntegerField(blank=True, null=True, default=None)
    town = models.CharField(blank=True, null=True, default=None)
    
    def __str__(self) -> str:
        return self.username