from users.factories import AreaFactory, AreaEmployeeFactory
from core.factories import CourseFactory, ClassroomFactory, ClassroomStudentFactory, SubjectFactory
from users.models import Area
import random


def create_areas(command):
    command.print('Creating areas...')

    areas = list()

    for _ in range(command.size):
        area = AreaFactory()
        areas.append(area)

    command.cache['areas'] = areas


def create_areas_employees(command):
    command.print('Attaching employees to areas...')

    area_employees = list()
    areas = Area.objects.all()
    command.cache['areas'] = areas
    for area in areas:
        for _ in range(command.size):
            employee = AreaEmployeeFactory(area=area,
                                           employee=random.choice(command.cache['employees']))
            area_employees.append(employee)

    command.cache['area_employees'] = area_employees

def create_courses(command):
    command.print('Creating courses...')

    courses = list()

    for _ in range(command.size):
        coordenator = random.choice(command.cache['coordenators'])
        course = CourseFactory(coordenator=coordenator)
        courses.append(course)

    command.cache['courses'] = courses

def create_subjects(command):
    command.print('Creating subjects...')

    subjects = list()

    for course in command.cache['courses']:
        for _ in range(command.size * 5):
            teacher = random.choice(command.cache['teachers'])
            subject = SubjectFactory(teacher=teacher, course=course)
            subjects.append(subject)

    command.cache['subjects'] = subjects

def create_classroom(command):
    command.print('Creating classrooms...')

    classrooms = list()

    for _ in range(command.size):
        course = random.choice(command.cache['courses'])
        classroom = ClassroomFactory(course=course)
        classrooms.append(classroom)

    command.cache['classrooms'] = classrooms


def create_classroom_students(command):
    command.print('Attaching students to classrooms...')

    classroom_students = list()
    students = command.cache['students']
    classrooms = command.cache['classrooms']
    start, end = 0, int(len(students) / len(classrooms))
    for classroom in classrooms:
        for student in students[start:end]:
            classroom_student = ClassroomStudentFactory(student=student,
                                                        classroom=classroom)
            classroom_students.append(classroom_student)
        start, end = end, end * 2
    command.cache['classroom_students'] = classroom_students
