from django.contrib import admin
from .models import (Joint_Screw, Joint_Denavit,
                     Joint_Screw_User, Joint_Denavit_User)


admin.site.register(Joint_Screw)
admin.site.register(Joint_Denavit)
admin.site.register(Joint_Screw_User)
admin.site.register(Joint_Denavit_User)
