from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm


class bid(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    # tg = models.CharField(max_length=20, blank=True, null=True)


# class User(AbstractUser):
#     alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', message='Only alphanumeric characters are allowed.')
#     username = models.CharField(max_length=20)
#     email = models.EmailField(max_length=40)
#     password = models.CharField(max_length=32)


class Registration(models.Model):
    email = models.CharField(max_length=40)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=32)

    user = models.OneToOneField(User, on_delete=models.CASCADE)


