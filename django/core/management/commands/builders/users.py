from users.factories import UserFactory
from core import defaults


def create_teachers(command):
    command.print('Creating teachers...')

    teachers = list()

    for _ in range(command.size * 5):
        user = UserFactory(role=defaults.USER_ROLE_TEACHER)
        teachers.append(user)

    command.cache['teachers'] = teachers


def create_employees(command):
    command.print('Creating employees...')

    employees = list()

    for _ in range(command.size * 10):
        user = UserFactory(role=defaults.USER_ROLE_EMPLOYEE)
        employees.append(user)

    command.cache['employees'] = employees


def create_coordenators(command):
    command.print('Creating coordenators...')

    coordenators = list()

    for _ in range(command.size):
        user = UserFactory(role=defaults.USER_ROLE_CORDENATOR)
        coordenators.append(user)

    command.cache['coordenators'] = coordenators


def create_students(command):
    command.print('Creating students...')

    students = list()

    for _ in range(command.size * 50):
        user = UserFactory(role=defaults.USER_ROLE_STUDENT)
        students.append(user)

    command.cache['students'] = students
