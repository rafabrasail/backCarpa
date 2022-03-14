from ctypes.wintypes import POINT
from django.contrib import admin
from .models import (Robot, RobotDefault)


admin.site.register(Robot)
admin.site.register(RobotDefault)


