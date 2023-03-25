from django import forms
from questions.models import Question


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
<<<<<<< HEAD
        fields = ['description', 'axis', 'answer_type']
=======
        fields = ['description', 'axis', 'answer_type']
>>>>>>> 85ecdf2 (feat:resolução de bugs)
