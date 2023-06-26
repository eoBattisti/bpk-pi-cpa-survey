from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy

from .models import Exam

from .forms import ExamForm

class ExamListView(ListView):
    model = Exam
    template_name = 'list/exams_form.html'


class ExamCreateView(CreateView):
    model = Exam
    template_name = 'form/exams_editor.html'
    form_class = ExamForm
    success_url = reverse_lazy('exam:list')


class ExamUpdateView(UpdateView):
    model = Exam
    template_name = 'form/exams_editor.html'
    form_class = ExamForm
    success_url = reverse_lazy('exam:list')

