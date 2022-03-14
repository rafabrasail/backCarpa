from django.contrib import admin
from .models import (JointDenavit,
                     JointScrew,
                     JointScrewDefault,
                     JointDenavitDefault)


admin.site.register(JointDenavit)
admin.site.register(JointScrew)
admin.site.register(JointScrewDefault)
admin.site.register(JointDenavitDefault)
