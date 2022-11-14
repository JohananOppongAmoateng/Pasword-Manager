from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404,get_list_or_404
from .serializers import PasswordInfoSerializer
from .models import PasswordInfo



class AddPasswordInfo(APIView):
    """
    Add new password information
    """
    def post(self,request):
        serializer = PasswordInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RetrievePasswordInfo(APIView):
    """
    Retrieves password information using an id
    """
    def get(self,request,id):
        passwordinfo = get_object_or_404(PasswordInfo,pk=id,user=request.user)
        serializer = PasswordInfoSerializer(passwordinfo)
        return Response(serializer.data)


class UpdatePasswordInfo(APIView):
    """
    Updates specific password information using an id
    """
    def put(self,request,id):
        passwordinfo = get_object_or_404(PasswordInfo,pk=id,user=request.user)
        serializer = PasswordInfoSerializer(passwordinfo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class PasswordInfoList(APIView):
    def get(self,request):
        passwordinfolist = get_list_or_404(PasswordInfo,user=request.user)
        serializer = PasswordInfoSerializer(passwordinfolist)
        return Response(serializer.data)


class DeletePasswordInfo(APIView):
    def delete(self,request,id):
        passwordinfo = get_object_or_404(PasswordInfo,pk=id,user=request.user)
        passwordinfo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        
