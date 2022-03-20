from msilib.schema import ServiceInstall
from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import (
    RobotSerializer, Robot_UserSerializer, UserCustomSerializer)
from .models import (Robot, Robot_User, UserCustom)


class RobotViewSet(viewsets.ModelViewSet):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer


class Robot_UserViewSet(viewsets.ModelViewSet):
    queryset = Robot_User.objects.all()
    serializer_class = Robot_UserSerializer


class UserCustomViewSet(viewsets.ModelViewSet):
    queryset = UserCustom.objects.all()
    serializer_class = UserCustomSerializer






