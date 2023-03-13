from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, ListView, UpdateView, View, FormView)

from axis.models import Axle

class AxleListView(ListView):
    model = Axle
    template_name = 'lists/list.html'
