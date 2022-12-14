"""password_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from rest_framework.schemas import get_schema_view
# from django.views.generic import TemplateView
# from rest_framework.documentation import include_docs_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path("authentication/",include("authentication.urls")),
    path('passwordmanager/v0.0.1/',include("PasswordInfo.urls")),
    # path('docs',include_docs_urls(title='Password Manager')),
    # path('openapi', get_schema_view(
    #     description="API for saving passwords",
    #      title="Password Manager",
    #    version="0.0.1"
    # ), name='openapi-schema'),

    # path('api/', TemplateView.as_view(
    #     template_name='swagger-ui.html',
    #     extra_context={'schema_url':'openapi-schema'}
    # ), name='swagger-ui'),
]