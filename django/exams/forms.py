from django import forms
from exams.models import Exam
from users.models import User
from questions.models import Question

class ExamForm(forms.ModelForm):
    responsible = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label='Responsável',
        required=True,
        empty_label='Selecione um responsável',
    )

    class Meta:
        model = Exam
        fields = ['title', 'start_date', 'end_date', 'responsible', 'area', 'subject']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_date'].widget.attrs = {
        'class': 'form-control',
        'placeholder': 'Escolha data e hora (inicial)',
        'id': 'kt_datepicker_3',
    }
        self.fields['end_date'].widget.attrs = {
        'class': 'form-control',
        'placeholder': 'Escolha data e hora (final)',
        'id': 'kt_datepicker_4',
    }

    