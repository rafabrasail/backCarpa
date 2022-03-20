from msilib.schema import ServiceInstall
from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import (PointSerializer, PointUserSerializer)
from .models import (Point, PointUser)


class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer


class PointUserViewSet(viewsets.ModelViewSet):
    queryset = PointUser.objects.all()
    serializer_class = PointUserSerializer
