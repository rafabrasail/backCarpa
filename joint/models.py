from statistics import mode
from django.db import models


class Joint(models.Model):
    type_joint = (
        ("T", 'translation'),
        ("R", 'rotation')
    )

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=1, choices=type_joint, default="R")
    screw_s_x = models.FloatField(default=0.0)
    screw_s_y = models.FloatField(default=0.0)
    screw_s_z = models.FloatField(default=0.0)
    screw_s0_x = models.FloatField(default=0.0)
    screw_s0_y = models.FloatField(default=0.0)
    screw_s0_z = models.FloatField(default=0.0)
    screw_t = models.FloatField(default=0.0)
    screw_theta = models.FloatField(default=0.0)
    denavit_alpha = models.FloatField(default=0.0)
    denavit_a = models.FloatField(default=0.0)
    denavit_d = models.FloatField(default=0.0)
    denavit_theta = models.FloatField(default=0.0)
    file = models.FileField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.name


class Joint_User(models.Model):
    type_joint = (
        ("T", 'translation'),
        ("R", 'rotation')
    )

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=1, choices=type_joint, default="R")
    screw_s_x = models.FloatField(default=0.0)
    screw_s_y = models.FloatField(default=0.0)
    screw_s_z = models.FloatField(default=0.0)
    screw_s0_x = models.FloatField(default=0.0)
    screw_s0_y = models.FloatField(default=0.0)
    screw_s0_z = models.FloatField(default=0.0)
    screw_t = models.FloatField(default=0.0)
    screw_theta = models.FloatField(default=0.0)
    denavit_alpha = models.FloatField(default=0.0)
    denavit_a = models.FloatField(default=0.0)
    denavit_d = models.FloatField(default=0.0)
    denavit_theta = models.FloatField(default=0.0)
    file = models.FileField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.name