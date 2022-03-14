from rest_framework import serializers
from .models import Robot, RobotDefault, UserCustom


class RobotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Robot
        fields = ['url', 'owner', 'name']


class RobotDefaultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RobotDefault
        fields = ['url', 'name']


class UserCustomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserCustom
        fields = ['url', 'nome', 'institute', 'user', 'robots']





