from django.db import models
from django.contrib.auth.models import User

class RobotDefault(models.Model):
    name = models.CharField(max_length=200)
    jointDenavit = models.ManyToManyField(
        'joint.JointDenavitDefault', related_name='jointDenavitDefault_robot', null=True, blank=True)
    jointScrew = models.ManyToManyField(
        'joint.JointScrewDefault', related_name='jointScrewDefault_robot', null=True, blank=True)
    points = models.ManyToManyField(
        'point.PointDefault', related_name='pointDefault_robot', null=True, blank=True)

    def __str__(self):
        return self.name


class Robot(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    jointDenavit = models.ManyToManyField(
        'joint.JointDenavit', related_name='jointDenavit_robot', null=True, blank=True)
    jointScrew = models.ManyToManyField(
        'joint.JointScrew', related_name='jointScrew_robot', null=True, blank=True)
    points = models.ManyToManyField(
        'point.Point', related_name='point_robot', null=True, blank=True)

    def __str__(self):
        return self.name


class UserCustom(models.Model):
    nome = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    robots = models.ManyToManyField(Robot)

    def __str__(self):
        return self.name    





    


    








    
