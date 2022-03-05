from ctypes.wintypes import POINT
from django.contrib import admin
from .models import (JointDenavit, JointScrew, Point,
                     Robot, RobotDefault, JointScrewDefault, JointDenavitDefault, PointDefault)


admin.site.register(JointDenavit)
admin.site.register(JointScrew)
admin.site.register(Point)
admin.site.register(Robot)
admin.site.register(RobotDefault)
admin.site.register(JointScrewDefault)
admin.site.register(JointDenavitDefault)
admin.site.register(PointDefault)
