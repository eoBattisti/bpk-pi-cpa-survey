from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from axis.forms import AxleForm
from axis.models import Axle


class AxleListView(ListView):
    model = Axle
    template_name = 'list/axle_list.html'


class AxleCreateView(CreateView):
    model = Axle
    template_name = 'form/axle_editor.html'
    form_class = AxleForm
    success_url = reverse_lazy('axis:list')


class AxleUpdateView(UpdateView):
    model = Axle
    template_name = 'form/axle_editor.html'
    form_class = AxleForm
    success_url = reverse_lazy('axis:list')
