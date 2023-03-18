from django.contrib import admin

from exams.models import Exam, ExamQuestion, Answer


admin.site.register(Exam)
admin.site.register(ExamQuestion)
admin.site.register(Answer)
