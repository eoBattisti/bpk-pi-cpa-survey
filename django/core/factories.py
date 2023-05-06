import factory

from core.models import Classroom, ClassroomStudent, Course, Subject
from users.factories import UserFactory


class CourseFactory(factory.django.DjangoModelFactory):

    title = factory.Faker('sentence', nb_words=3, locale='pt_BR')
    alias = factory.Faker('sentence', nb_words=1, ext_word_list=["ADS", "FAR",
                                                                 "CD", "ES"])
    coordenator = factory.SubFactory(UserFactory)

    class Meta:
        model = Course
        django_get_or_create = ('title',)


class ClassroomFactory(factory.django.DjangoModelFactory):

    title = factory.Faker('sentence', nb_words=2, locale='pt_BR')
    start_date = factory.Faker('date_this_year')
    end_date = factory.Faker('date_this_year')
    course = factory.SubFactory(CourseFactory)

    class Meta:
        model = Classroom
        django_get_or_create = ('title', 'course',)


class ClassroomStudentFactory(factory.django.DjangoModelFactory):

    classroom = factory.SubFactory(ClassroomFactory)
    student = factory.SubFactory(UserFactory)

    class Meta:
        model = ClassroomStudent
        django_get_or_create = ('classroom', 'student',)


class SubjectFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('sentence', nb_words=1, locale='pt_BR')
    course = factory.SubFactory(CourseFactory)
    teacher = factory.SubFactory(UserFactory)

    class Meta:
        model = Subject
        django_get_or_create = ('title', 'teacher',)
