from django.contrib import admin

from users.models import User, Area, AreaEmployee


admin.site.register(User)
admin.site.register(Area)
admin.site.register(AreaEmployee)
