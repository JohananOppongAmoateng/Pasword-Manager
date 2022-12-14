from django.db import models
from django.contrib.auth import get_user_model
from django_cryptography.fields import encrypt

# Create your models here.

class PasswordInfo(models.Model):
    """
        PasswordInfo model
    """
    password = encrypt(models.CharField(max_length=200))
    organization = encrypt(models.CharField(max_length=25))
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="passwordinfos")
    username = encrypt(models.CharField(max_length=60))

    def __str__(self):
        return self.password

    