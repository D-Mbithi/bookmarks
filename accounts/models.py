from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    location = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.username