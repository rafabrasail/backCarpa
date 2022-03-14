from rest_framework import serializers
from .models import Point, PointDefault



class PointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Point
        fields = ['url', 'robot', 'owner', 'name', 'position_x',
                  'position_y', 'position_z', 'orientation_x', 'orientation_y', 'orientation_z']


class PointDefaultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PointDefault
        fields = ['url', 'robot', 'owner', 'name', 'position_x',
                  'position_y', 'position_z', 'orientation_x', 'orientation_y', 'orientation_z']
