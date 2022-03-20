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
from core.views import (RobotViewSet, Robot_UserViewSet, UserCustomViewSet)
from joint.views import (Joint_ScrewViewSet, Joint_DenavitViewSet,
                         Joint_Screw_UserViewSet, Joint_Denavit_UserViewSet)
from point.views import (PointViewSet, PointUserViewSet)
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'Joint_Screw', Joint_ScrewViewSet)
router.register(r'Joint_Denavit', Joint_DenavitViewSet)
router.register(r'Joint_Screw_User', Joint_Screw_UserViewSet)
router.register(r'Joint_Denavit_User', Joint_Denavit_UserViewSet)
router.register(r'Point', PointViewSet)
router.register(r'Point_User', PointUserViewSet)
router.register(r'Robot', RobotViewSet)
router.register(r'Robot_User', Robot_UserViewSet)
router.register(r'UserCustom', UserCustomViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', views.obtain_auth_token, name='api-token-auth'),
]
