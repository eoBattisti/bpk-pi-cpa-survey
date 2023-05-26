from rest_framework import serializers

from core.models import Classroom, Course, Subject


class ClassroomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classroom
        fields = '__all__'
        datatables_always_serialize = ('id',)


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'
        datatables_always_serialize = ('id',)


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'
        datatables_always_serialize = ('id',)
