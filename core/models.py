from django.db import models
from django.contrib.auth.models import User


class Robot(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class RobotDefault(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name        


class JointScrew(models.Model):
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    s_x = models.FloatField(default=0.0)
    s_y = models.FloatField(default=0.0)
    s_z = models.FloatField(default=0.0)
    s0_x = models.FloatField(default=0.0)
    s0_y = models.FloatField(default=0.0)
    s0_z = models.FloatField(default=0.0)
    t = models.FloatField(default=0.0)
    theta = models.FloatField(default=0.0)
    # file = models.FileField()

    def __str__(self):
        return self.name


class JointScrewDefault(models.Model):
    robot = models.ForeignKey(RobotDefault, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    s_x = models.FloatField(default=0.0)
    s_y = models.FloatField(default=0.0)
    s_z = models.FloatField(default=0.0)
    s0_x = models.FloatField(default=0.0)
    s0_y = models.FloatField(default=0.0)
    s0_z = models.FloatField(default=0.0)
    t = models.FloatField(default=0.0)
    theta = models.FloatField(default=0.0)
    # file = models.FileField()

    def __str__(self):
        return self.name        



class JointDenavit(models.Model):
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    alpha = models.FloatField(default=0.0)
    a = models.FloatField(default=0.0)
    d = models.FloatField(default=0.0)
    theta = models.FloatField(default=0.0)
    # file = models.FileField()

    def __str__(self):
        return self.name


class JointDenavitDefault(models.Model):
    robot = models.ForeignKey(RobotDefault, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    alpha = models.FloatField(default=0.0)
    a = models.FloatField(default=0.0)
    d = models.FloatField(default=0.0)
    theta = models.FloatField(default=0.0)
    # file = models.FileField()

    def __str__(self):
        return self.name        


class Point(models.Model):
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    position_x = models.FloatField(default=0.0)
    position_y = models.FloatField(default=0.0)
    position_z = models.FloatField(default=0.0)
    orientation_x = models.FloatField(default=0.0)
    orientation_y = models.FloatField(default=0.0)
    orientation_z = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class PointDefault(models.Model):
    robot = models.ForeignKey(RobotDefault, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    position_x = models.FloatField(default=0.0)
    position_y = models.FloatField(default=0.0)
    position_z = models.FloatField(default=0.0)
    orientation_x = models.FloatField(default=0.0)
    orientation_y = models.FloatField(default=0.0)
    orientation_z = models.FloatField(default=0.0)

    def __str__(self):
        return self.name





    
