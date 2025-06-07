from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from common.models import BaseModel
from users.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_confirmed = models.BooleanField(default=False)
    is_organizer = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email