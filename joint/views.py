from msilib.schema import ServiceInstall
from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import (JointSerializer, Joint_UserSerializer)
from .models import (Joint, Joint_User)


class JointViewSet(viewsets.ModelViewSet):
    queryset = Joint.objects.all()
    serializer_class = JointSerializer


class Joint_UserViewSet(viewsets.ModelViewSet):
    queryset = Joint_User.objects.all()
    serializer_class = Joint_UserSerializer
