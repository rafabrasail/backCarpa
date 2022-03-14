from rest_framework import serializers
from .models import JointDenavit, JointScrew, JointDenavitDefault, JointScrewDefault


class JointDenavitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JointDenavit
        fields = ['url', 'robot', 'name', 'alpha', 'a', 'd', 'theta']


class JointDenavitDefaultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JointDenavitDefault
        fields = ['url', 'robot', 'name', 'alpha', 'a', 'd', 'theta']


class JointScrewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JointScrew
        fields = ['url', 'robot ', 'name', 's_x', 's_y', 's_z',
                  's0_x', 's0_y', 's0_z', 't', 'theta']


class JointScrewDefaultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JointScrewDefault
        fields = ['url', 'robot', 'name', 's_x', 's_y', 's_z',
                  's0_x', 's0_y', 's0_z', 't', 'theta']
