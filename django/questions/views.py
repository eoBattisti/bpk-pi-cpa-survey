from django.views.generic import ListView, CreateView, UpdateView
from questions.models import Question
from questions.forms import QuestionForm
from django.urls import reverse_lazy

class QuestionsListView(ListView):

    model = Question
    template_name = 'list/questions_list.html'

class QuestionsCreateView(CreateView):

    model = Question
    template_name = 'form/questions_editor.html'
    form_class = QuestionForm
    success_url = reverse_lazy("questions:list")

class QuestionsUpdateView(UpdateView):

    model = Question
    template_name = 'form/questions_editor.html'
    form_class = QuestionForm
    success_url = reverse_lazy("questions:list")

