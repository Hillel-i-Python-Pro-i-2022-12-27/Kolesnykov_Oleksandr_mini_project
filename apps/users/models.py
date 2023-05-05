from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class User(AbstractUser, PermissionsMixin):
    image = models.ImageField(upload_to="user_photo", null=True, blank=True)
