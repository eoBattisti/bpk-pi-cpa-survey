import random
from core import defaults
from core.models import ClassroomStudent
from exams.factories import AnswersFactory, ExamFactory, ExamQuestionFactory
from exams.models import Exam
from users.models import User

def create_exams(command):
    command.print('Creating exams...')

    exams = list()

    for _ in range(command.size):
        responsible = random.choice(command.cache['teachers'])
        subjects = command.cache['subjects']
        for subject in subjects:
            exam = ExamFactory(responsible=responsible,
                               area=random.choice(command.cache['areas']),
                               subject=subject)
            exams.append(exam)

    command.cache['exams'] = exams


def create_exams_questions(command):
    command.print('Attaching questions to exams...')

    exam_questions = list()

    for exam in command.cache['exams']:
        for _ in range(command.size * 5):
            exam_question = ExamQuestionFactory(exam=exam,
                                                question=random.choice(command.cache['questions']))
            exam_questions.append(exam_question)

    command.cache['exam_questions'] = exam_questions


def create_answers(command):
    command.print('Creating answers...')

    answers = list ()
    # try:

    for user in User.objects.filter(role=defaults.USER_ROLE_STUDENT):
        classroom_student = ClassroomStudent.objects.filter(student=user).first()
        subjects = classroom_student.classroom.course.subjects.all()
        exam = Exam.objects.filter(subject__in=subjects).first()
        if not exam:
            continue
        exam_questions = exam.questions.all()
        for exam_question in exam_questions:
            if exam_question.question.answer_type == defaults.ANSWER_TYPE_OBJECTIVE:
                answer = AnswersFactory(description=None,
                                        exam_question=exam_question,
                                        answerd_by=user)
            else:
                answer = AnswersFactory(exam_question=exam_question,
                                        value=0,
                                        answerd_by=user)
            answers.append(answer)

    # except Exception:
    #     pass

    # command.cache['answers'] = answers
