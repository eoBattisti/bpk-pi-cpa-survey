from django.contrib import admin

from core.models import Classroom, Course, Subject, ClassroomStudent


admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Classroom)
admin.site.register(ClassroomStudent)
