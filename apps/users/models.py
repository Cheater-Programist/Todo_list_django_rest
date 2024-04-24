from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, verbose_name='Phone number')
    age = models.IntegerField(verbose_name='Age')

    def __str__(self) -> str:
        return self.username
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'