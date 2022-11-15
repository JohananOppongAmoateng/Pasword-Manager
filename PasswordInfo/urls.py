from django.urls import path
from .views import PasswordInfoList,AddPasswordInfo,DeletePasswordInfo,RetrievePasswordInfo,UpdatePasswordInfo


urlpatterns = [
    path("addpassword",AddPasswordInfo.as_view()),
    path("passwords",PasswordInfoList.as_view()),
    path('password/<int:pk>',RetrievePasswordInfo.as_view()),
    path('password/delete/<int:pk>',DeletePasswordInfo.as_view()),
    path('password/edit/<int:pk>',UpdatePasswordInfo.as_view())
]