"""dt_test_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# from api.views import DataViewSet
from api import views

router = routers.DefaultRouter()

# router.register('alldata', DataViewSet, basename='data')
# router.register('ping', DataViewSet, basename='ping')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/alldata/', views.PostListView.as_view(), name=None),
    path('api/ping/', views.PostPingView, name=None),
    path('api/add/<int:pk>/', views.PostAddView.as_view(), name=None),
    path('api/substract/<int:pk>/', views.PostSubstractView.as_view(), name=None),
    path('api/status/<int:pk>/', views.PostStatusView.as_view(), name=None),
    path('admin/', admin.site.urls),
]
