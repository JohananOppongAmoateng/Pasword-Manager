from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PasswordInfo

class PasswordInfoSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = PasswordInfo
        fields = ["id","username","password","user","organization"]
