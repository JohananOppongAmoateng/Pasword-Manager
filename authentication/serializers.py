from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework  import serializers


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(TokenObtainPairSerializer,cls).get_token(user)
        token['username'] = user.username
        return token


class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True,validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(required = True,write_only=True,validators=[validate_password]
    )
    password2 = serializers.CharField(required = True,write_only=True)

    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password","password2"]

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Password fields did not match")
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user