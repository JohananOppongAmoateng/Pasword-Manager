from rest_framework import serializers
from .models import PasswordInfo

class PasswordInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordInfo
        fields = ["id","username","password","user","organization",]