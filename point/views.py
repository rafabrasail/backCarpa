from msilib.schema import ServiceInstall
from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import (PointSerializer,
                          PointDefaultSerializer)
from .models import (Point,
                     PointDefault)


class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer


class PointDefaultViewSet(viewsets.ModelViewSet):
    queryset = PointDefault.objects.all()
    serializer_class = PointDefaultSerializer
