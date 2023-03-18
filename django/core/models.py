import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    """ Model base para criar diversos outros models. """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(verbose_name=_("Created at"), auto_now=True)
    updated_at = models.DateTimeField(verbose_name=_("Updated at"), auto_now=True)

    class Meta:
        abstract = True


class Course(BaseModel):
    """Model para representar um curso"""
    title = models.CharField(verbose_name=_("Title"), max_length=75)
    alias = models.CharField(verbose_name=_("Alias"), max_length=5)
    coordenator = models.ForeignKey("users.User",
                                    verbose_name=_("Coordenator"),
                                    related_name="courses",
                                    on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")

    def __str__(self) -> str:
        return f'{self.alias} - {self.title} - {self.coordenator}'


class Subject(BaseModel):
    """ Model para representar uma disciplina."""
    title = models.CharField(verbose_name=_("Title"), max_length=50)
    course = models.ForeignKey("core.Course",
                               verbose_name=_("Course"),
                               related_name="subjects",
                               on_delete=models.CASCADE)
    teacher = models.ForeignKey("users.User",
                                verbose_name=_("Teacher"),
                                related_name="subjects",
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Subject")
        verbose_name_plural = _("Subjects")

    def __str__(self) -> str:
        return f'{self.course.alias} - {self.title}'


class Classroom(BaseModel):
    """Model para representar uma sala de aula - turma."""
    title = models.CharField(verbose_name=_("Title"), max_length=75)
    start_date = models.DateTimeField(verbose_name=_("Start date"))
    end_date = models.DateTimeField(verbose_name=_("End date"))
    course = models.ForeignKey("core.Course",
                               verbose_name=_("Course"),
                               related_name="classrooms",
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Classroom")
        verbose_name_plural = _("Classrooms")

    def __str__(self) -> str:
        return self.title


class ClassroomStudent(BaseModel):
    """Model para fazer a ligação n -> n de aluno e turma"""
    classroom = models.ForeignKey("core.Classroom",
                                  verbose_name=_("Classroom"),
                                  related_name="students",
                                  on_delete=models.CASCADE)
    student = models.ForeignKey("users.User",
                                verbose_name=_("Student"),
                                related_name="classrom",
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("ClassroomStudent")
        verbose_name_plural = _("ClassroomStudents")

    def __str__(self) -> str:
        return f'{self.classroom} - {self.student}'
