from crispy_forms.helper import FormHelper

from django import forms
from questions.models import Question


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['description', 'axis', 'answer_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['axis'].widget.attrs['data-control'] = 'select2'
        self.fields['axis'].widget.attrs['data-placeholder'] = 'Selecione um eixo'



    