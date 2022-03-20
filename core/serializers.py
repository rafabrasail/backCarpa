from rest_framework import serializers
from .models import (Robot, Robot_User, UserCustom)


class RobotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Robot
        fields = ['id', 'url', 'name', 
                  'jointsScrew', 'jointsDenavit', 'points']


class Robot_UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Robot_User
        fields = ['id', 'url', 'name',
                  'jointsScrew', 'jointsDenavit', 'points']


class UserCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustom
        fields = ['id', 'url', 'nome', 'institute', 'user', 'robots']