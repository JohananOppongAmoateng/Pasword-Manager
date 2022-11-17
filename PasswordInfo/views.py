from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.generics import CreateAPIView, DestroyAPIView,ListAPIView, RetrieveAPIView,UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwner
from .models import PasswordInfo
from .serializers import PasswordInfoSerializer

class PasswordInfoList(ListAPIView):
    queryset = PasswordInfo.objects.all()
    serializer_class = PasswordInfoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = PasswordInfo.objects.filter(user=user)
        return queryset


class UpdatePasswordInfo(UpdateAPIView):
    queryset = PasswordInfo.objects.all()
    serializer_class = PasswordInfoSerializer
    permission_classes = [IsAuthenticated,IsOwner]

    def get_object(self):
        queryset = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request,queryset)
        return queryset

class AddPasswordInfo(CreateAPIView):
    queryset = PasswordInfo.objects.all()
    serializer_class = PasswordInfoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RetrievePasswordInfo(RetrieveAPIView):
    queryset = PasswordInfo.objects.all()
    serializer_class = PasswordInfoSerializer
    permission_classes = [IsAuthenticated,IsOwner]

    def get_object(self):
        
        queryset = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request,queryset)
        return queryset


class DeletePasswordInfo(DestroyAPIView):
    queryset = PasswordInfo.objects.all()
    serializer_class = PasswordInfoSerializer
    permission_classes =[IsAuthenticated,IsOwner]


    def get_object(self):        
        queryset = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request,queryset)
        return queryset
    
    