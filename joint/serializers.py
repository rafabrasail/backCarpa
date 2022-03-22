from rest_framework import serializers
from .models import (Joint, Joint_User)


class JointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joint
        fields = ['id', 'url', 'name', 'type', 'screw_s_x', 'screw_s_y',
                  'screw_s_z', 'screw_s0_x', 'screw_s0_y', 'screw_s0_z', 
                  'screw_t', 'screw_theta', 'denavit_alpha', 'denavit_a', 
                  'denavit_d', 'denavit_theta', 'file']


class Joint_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joint_User
        fields = ['id', 'url', 'name', 'type', 'screw_s_x', 'screw_s_y',
                  'screw_s_z', 'screw_s0_x', 'screw_s0_y', 'screw_s0_z',
                  'screw_t', 'screw_theta', 'denavit_alpha', 'denavit_a',
                  'denavit_d', 'denavit_theta', 'file']










