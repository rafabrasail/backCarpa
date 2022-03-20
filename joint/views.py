from msilib.schema import ServiceInstall
from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import (Joint_ScrewSerializer, Joint_DenavitSerializer, 
                            Joint_Screw_UserSerializer, Joint_Denavit_UserSerializer)
from .models import (Joint_Screw, Joint_Denavit,
                     Joint_Screw_User, Joint_Denavit_User)


class Joint_ScrewViewSet(viewsets.ModelViewSet):
    queryset = Joint_Screw.objects.all()
    serializer_class = Joint_ScrewSerializer


class Joint_DenavitViewSet(viewsets.ModelViewSet):
    queryset = Joint_Denavit.objects.all()
    serializer_class = Joint_DenavitSerializer


class Joint_Screw_UserViewSet(viewsets.ModelViewSet):
    queryset = Joint_Screw_User.objects.all()
    serializer_class = Joint_Screw_UserSerializer


class Joint_Denavit_UserViewSet(viewsets.ModelViewSet):
    queryset = Joint_Denavit_User.objects.all()
    serializer_class = Joint_Denavit_UserSerializer