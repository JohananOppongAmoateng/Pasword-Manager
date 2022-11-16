from rest_framework_simplejwt.views import token_refresh
from .views import MyTokenObtainPairView,RegisterUserView
from django.urls import path

urlpatterns = [
    path("login",MyTokenObtainPairView.as_view(),name="token_obtain_pair"),
    path("login/refresh",token_refresh,name="token_refresh"),
    path("signup",RegisterUserView.as_view(),name="signup")
]