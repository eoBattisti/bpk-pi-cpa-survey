from django.utils.translation import gettext_lazy as _

USER_ROLE_CORDENATOR = 0
USER_ROLE_STUDENT = 1
USER_ROLE_EMPLOYEE = 2
USER_ROLE_TEACHER = 3
USER_ROLES = (
    (USER_ROLE_CORDENATOR, _('Coordenador')),
    (USER_ROLE_STUDENT, _('Aluno')),
    (USER_ROLE_EMPLOYEE, _('Funcionário')),
    (USER_ROLE_TEACHER, _('Professor')),
)

ANSWER_TYPE_DESCRIPTIVE = 0
ANSWER_TYPE_OBJECTIVE = 1
ANSWER_TYPES = (
    (ANSWER_TYPE_DESCRIPTIVE, _('Descritiva')),
    (ANSWER_TYPE_OBJECTIVE, _('Objetiva')),
)
