from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from .manager import MyUserManager


class Book(models.Model):
    title = models.EmailField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True,)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager() #new

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin