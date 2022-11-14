from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,RetrieveAPIView,UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_list_or_404,get_object_or_404
from .serializers import PasswordInfoSerializer
from .models import PasswordInfo


class PasswordInfoList(ListAPIView):
    queryset = PasswordInfo.objects.all()
    serializer_class = PasswordInfoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return get_list_or_404(PasswordInfo,user=user)

class AddPasswordInfo(CreateAPIView):
    queryset = PasswordInfo.objects.all()
    serializer_class = PasswordInfoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RetrievePasswordInfo(RetrieveAPIView):
    queryset = PasswordInfo.objects.all()
    serializer_class = PasswordInfoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        pk = self.kwargs['pk']
        return get_object_or_404(PasswordInfo,pk=pk,user=user)

class UpdatePasswordInfo(UpdateAPIView):
    queryset = PasswordInfo.objects.all()
    serializer_class = PasswordInfoSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        pk = self.kwargs['pk']
        return get_object_or_404(PasswordInfo,pk=pk,user=user)

class DeletePasswordInfo(DestroyAPIView):
    queryset = PasswordInfo.objects.all()
    serializer_class = PasswordInfoSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        pk = self.kwargs['pk']
        return get_object_or_404(PasswordInfo,pk=pk,user=user)
