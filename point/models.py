from django.db import models
from core.models import RobotDefault, Robot


class Point(models.Model):
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE)
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
