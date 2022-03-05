from rest_framework import serializers
from .models import JointDenavit, JointScrew, Point, Robot, JointDenavitDefault, JointScrewDefault, PointDefault, RobotDefault


class RobotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Robot
        fields = ['owner', 'name']


class RobotDefaultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RobotDefault
        fields = ['name']


class JointDenavitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JointDenavit
        fields = ['robot', 'name', 'alpha', 'a', 'd', 'theta']


class JointDenavitDefaultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JointDenavitDefault
        fields = ['robot', 'name', 'alpha', 'a', 'd', 'theta']


class JointScrewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JointScrew
        fields = ['robot', 'name', 's_x', 's_y', 's_z',
                  's0_x', 's0_y', 's0_z', 't', 'theta']


class JointScrewDefaultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JointScrewDefault
        fields = ['robot', 'name', 's_x', 's_y', 's_z',
                  's0_x', 's0_y', 's0_z', 't', 'theta']


class PointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Point
        fields = ['robot', 'owner', 'name', 'position_x',
                  'position_y', 'position_z', 'orientation_x', 'orientation_y', 'orientation_z']


class PointDefaultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PointDefault
        fields = ['robot', 'owner', 'name', 'position_x',
                  'position_y', 'position_z', 'orientation_x', 'orientation_y', 'orientation_z']