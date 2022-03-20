from rest_framework import serializers
from .models import (Joint_Screw, Joint_Denavit,
                     Joint_Screw_User, Joint_Denavit_User)


class Joint_ScrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joint_Screw
        fields = ['id', 'url', 'name', 'type', 's_x', 's_y', 
                  's_z', 's0_x', 's0_y', 's0_z', 't', 'theta']


class Joint_DenavitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joint_Denavit
        fields = ['id', 'url', 'name', 'type', 'alpha', 'a', 'd', 'theta']


class Joint_Screw_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joint_Screw_User
        fields = ['id', 'url', 'name', 'type', 's_x', 's_y',
                  's_z', 's0_x', 's0_y', 's0_z', 't', 'theta']


class Joint_Denavit_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joint_Denavit_User
        fields = ['id', 'url', 'name', 'type', 'alpha', 'a', 'd', 'theta']




# class JointDenavitSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = JointDenavit
#         fields = '__all__'
#         # fields = ['url', 'robot', 'name', 'alpha', 'a', 'd', 'theta']


# class JointDenavitDefaultSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = JointDenavitDefault
#         fields = '__all__'
#         # fields = ['url', 'robot', 'name', 'alpha', 'a', 'd', 'theta']


# class JointScrewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = JointScrew
#         fields = '__all__'
#         # fields = ['url', 'robot ', 'name', 's_x', 's_y', 's_z',
#                 #   's0_x', 's0_y', 's0_z', 't', 'theta']



