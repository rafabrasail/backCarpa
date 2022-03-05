from msilib.schema import ServiceInstall
from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import (JointDenavitSerializer, 
                          JointScrewSerializer, 
                          PointSerializer, 
                          RobotSerializer, 
                          RobotDefaultSerializer, 
                          JointDenavitDefaultSerializer, 
                          JointScrewDefaultSerializer, 
                          PointDefaultSerializer)
from .models import (JointDenavit, 
                     JointScrew, 
                     Point, 
                     Robot, 
                     JointDenavitDefault, 
                     JointScrewDefault, 
                     PointDefault, 
                     RobotDefault)


class RobotViewSet(viewsets.ModelViewSet):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer


class RobotDefaultViewSet(viewsets.ModelViewSet):
    queryset = RobotDefault.objects.all()
    serializer_class = RobotDefaultSerializer


class JointDenavitViewSet(viewsets.ModelViewSet):
    queryset = JointDenavit.objects.all()
    serializer_class = JointDenavitSerializer


class JointDenavitDefaultViewSet(viewsets.ModelViewSet):
    queryset = JointDenavitDefault.objects.all()
    serializer_class = JointDenavitDefaultSerializer


class JointScrewViewSet(viewsets.ModelViewSet):
    queryset = JointScrew.objects.all()
    serializer_class = JointScrewSerializer


class JointScrewDefaultViewSet(viewsets.ModelViewSet):
    queryset = JointScrewDefault.objects.all()
    serializer_class = JointScrewDefaultSerializer


class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer


class PointDefaultViewSet(viewsets.ModelViewSet):
    queryset = PointDefault.objects.all()
    serializer_class = PointDefaultSerializer
