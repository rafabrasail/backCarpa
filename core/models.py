from django.db import models
from django.contrib.auth.models import User


class Robot(models.Model):
    name = models.CharField(max_length=200)
    jointsScrew = models.ManyToManyField(
        'joint.Joint_Screw', related_name='screw_list', blank=True)
    jointsDenavit = models.ManyToManyField(
        'joint.Joint_Denavit', related_name='screw_list', blank=True)
    points = models.ManyToManyField(
        'point.Point', related_name='listPoints', blank=True)

    def __str__(self):
        return self.name


class Robot_User(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    jointsScrew = models.ManyToManyField(
        'joint.Joint_Screw_User', related_name='screw_list', blank=True)
    jointsDenavit = models.ManyToManyField(
        'joint.Joint_Denavit_User', related_name='screw_list', blank=True)
    points = models.ManyToManyField(
        'point.PointUser', related_name='listPoints', blank=True)

    def __str__(self):
        return self.name


class UserCustom(models.Model):
    nome = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    robots = models.ManyToManyField(Robot)

    def __str__(self):
        return self.name    





    


    








    
