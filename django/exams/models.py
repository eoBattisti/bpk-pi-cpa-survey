from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel


class Exam(BaseModel):
    """Mode para representar uma avaliação"""
    title = models.CharField(verbose_name=_("Title"), max_length=50)
    start_date = models.DateTimeField(verbose_name=_("Start date"))
    end_date = models.DateTimeField(verbose_name=_("End date"))
    responsible = models.ForeignKey("users.User",
                                    verbose_name=_("Responsible"),
                                    related_name="exams",
                                    on_delete=models.CASCADE)
    area = models.ForeignKey("users.Area",
                             verbose_name=_("Area"),
                             related_name='exams',
                             on_delete=models.CASCADE,
                             null=True,
                             blank=True)
    subject = models.ForeignKey("core.Subject",
                                verbose_name=_("Subject"),
                                related_name="exams",
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)

    class Meta:
        verbose_name = _("Exam")
        verbose_name_plural = _("Exams")

    def __str__(self):
        return self.title


class ExamQuestion(BaseModel):
    """ Model para fazer a ligação n -> n de avaliações e perguntas"""
    exam = models.ForeignKey("exams.Exam",
                             verbose_name=_("Exam"),
                             related_name="answers",
                             on_delete=models.CASCADE)
    question = models.ForeignKey("questions.Question",
                                 verbose_name=_("Question"),
                                 related_name="exams",
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("ExamQuestion")
        verbose_name_plural = _("ExamQuestions")

    def __str__(self):
        return f'{self.exam} - {self.question}'


class Answer(BaseModel):
    """ Model para representar as respostas de uma pergunta"""
    description = models.TextField(verbose_name=_("Description"),
                                   null=True,
                                   blank=True)
    value = models.SmallIntegerField(verbose_name=_("Value"),
                                     null=True,
                                     blank=True)
    exam_question = models.ForeignKey("exams.ExamQuestion",
                                      verbose_name=_("Exam Question"),
                                      related_name="answer",
                                      on_delete=models.CASCADE)
    answerd_by = models.ForeignKey("users.User",
                                   verbose_name=_("Answered by"),
                                   related_name='answers',
                                   on_delete=models.CASCADE)
