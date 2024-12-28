from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    college = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
