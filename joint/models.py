from django.db import models
from core.models import RobotDefault, Robot


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
