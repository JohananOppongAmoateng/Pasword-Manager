from django.urls import path
from .views import PasswordInfoList,AddPasswordInfo,DeletePasswordInfo,RetrievePasswordInfo,UpdatePasswordInfo


urlpatterns = [
    path("addpassword",AddPasswordInfo.as_view(),name="addpassword"),
    path("passwords",PasswordInfoList.as_view(),name="passwordlist"),
    path('password/<int:pk>',RetrievePasswordInfo.as_view(),name="retrievepassword"),
    path('password/delete/<int:pk>',DeletePasswordInfo.as_view(),name="deletepassword"),
    path('password/edit/<int:pk>',UpdatePasswordInfo.as_view(),name="editpassword")
]