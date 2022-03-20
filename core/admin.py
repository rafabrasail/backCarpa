from ctypes.wintypes import POINT
from django.contrib import admin
from .models import (Robot, Robot_User, UserCustom)


admin.site.register(Robot)
admin.site.register(Robot_User)
admin.site.register(UserCustom)


