"""amtit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_jwt.views import obtain_jwt_token
schema_view = get_schema_view(
   openapi.Info(
      title="AMT3",
      default_version='v1',
      description="AMT3",
      license=openapi.License(name="License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/accounts/', include('accounts.urls')),
    path('api/problems/', include('problems.urls')),
    path('api/xnotes/', include('xnotes.urls')),
    path('api/interprobs/', include('interprobs.urls')),
    path('admin/', admin.site.urls),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('api/token/', obtain_jwt_token),
]
