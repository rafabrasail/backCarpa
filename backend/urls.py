"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from rest_framework import routers
from .views import UserViewSet, GroupViewSet
from core.views import (JointDenavitViewSet, 
                        JointScrewViewSet, 
                        PointViewSet, 
                        RobotViewSet, 
                        RobotDefaultViewSet, 
                        JointDenavitDefaultViewSet, 
                        JointScrewDefaultViewSet, 
                        PointDefaultViewSet)
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'JointDenavit', JointDenavitViewSet)
router.register(r'JointScrew', JointScrewViewSet)
router.register(r'Point', PointViewSet)
router.register(r'Robot', RobotViewSet)
router.register(r'JointDenavitDefault', JointDenavitDefaultViewSet)
router.register(r'JointScrewDefault', JointScrewDefaultViewSet)
router.register(r'PointDefault', PointDefaultViewSet)
router.register(r'RobotDefault', RobotDefaultViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', views.obtain_auth_token, name='api-token-auth'),
]
