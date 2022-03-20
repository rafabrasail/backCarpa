from statistics import mode
from django.db import models


class Joint_Screw(models.Model):
    type_joint = (
        ("T", 'translation'),
        ("R", 'rotation')
    )

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=1, choices=type_joint, default="R")
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


class Joint_Denavit(models.Model):
    type_joint = (
        ("T", 'translation'),
        ("R", 'rotation')
    )

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=1, choices=type_joint, default="R")
    alpha = models.FloatField(default=0.0)
    a = models.FloatField(default=0.0)
    d = models.FloatField(default=0.0)
    theta = models.FloatField(default=0.0)
    # file = models.FileField()

    def __str__(self):
        return self.name


class Joint_Screw_User(models.Model):
    type_joint = (
        ("T", 'translation'),
        ("R", 'rotation')
    )

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=1, choices=type_joint, default="R")
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


class Joint_Denavit_User(models.Model):
    type_joint = (
        ("T", 'translation'),
        ("R", 'rotation')
    )

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=1, choices=type_joint, default="R")
    alpha = models.FloatField(default=0.0)
    a = models.FloatField(default=0.0)
    d = models.FloatField(default=0.0)
    theta = models.FloatField(default=0.0)
    # file = models.FileField()

    def __str__(self):
        return self.name