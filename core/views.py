from msilib.schema import ServiceInstall
from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import (RobotSerializer, 
                          RobotDefaultSerializer, UserCustomSerializer)
from .models import (Robot, 
                     RobotDefault, UserCustom)


class RobotViewSet(viewsets.ModelViewSet):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer


class RobotDefaultViewSet(viewsets.ModelViewSet):
    queryset = RobotDefault.objects.all()
    serializer_class = RobotDefaultSerializer


class UserCustomViewSet(viewsets.ModelViewSet):
    queryset = UserCustom.objects.all()
    serializer_class = UserCustomSerializer






