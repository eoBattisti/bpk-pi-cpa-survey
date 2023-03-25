from django import forms
from questions.models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['description', 'axis', 'answer_type']