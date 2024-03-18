from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length = 60, blank = True, null = True)

    def __str__(self):
        return self.username