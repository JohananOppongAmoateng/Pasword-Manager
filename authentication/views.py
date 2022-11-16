# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer,RegisterUserSerializer

from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = MyTokenObtainPairSerializer


class RegisterUserView(APIView):
    def post(self,request,format=None):
        serializer = RegisterUserSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




