from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class PasswordInfo(models.Model):
    """
        PasswordInfo model
    """
    password = models.CharField(max_length=200)
    organization = models.CharField(max_length=25)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="passwordinfos")
    username = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.password

    