from rest_framework import serializers
from .models import (Point, PointUser)


class PointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Point
        fields = ['id', 'url', 'name', 'position_x', 'position_y',
                  'position_z', 'orientation_x', 'orientation_y', 'orientation_z']


class PointUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PointUser
        fields = ['id', 'url', 'name', 'position_x', 'position_y',
                  'position_z', 'orientation_x', 'orientation_y', 'orientation_z']
