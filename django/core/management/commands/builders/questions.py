from questions.factories import QuestionFactory


def create_questions(command):
    command.print('Creating questions...')

    questions = list()

    for _ in range(command.size * 2):
        for axis in command.cache['axis']:
            question = QuestionFactory(axis=axis)
            questions.append(question)

    command.cache['questions'] = questions
