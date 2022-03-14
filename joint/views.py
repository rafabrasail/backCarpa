from msilib.schema import ServiceInstall
from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import (JointDenavitSerializer,
                          JointScrewSerializer,
                          JointDenavitDefaultSerializer,
                          JointScrewDefaultSerializer)
from .models import (JointDenavit,
                     JointScrew,
                     JointDenavitDefault,
                     JointScrewDefault)


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
