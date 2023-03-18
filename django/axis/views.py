from django.views.generic import (ListView)

from axis.models import Axle


class AxleListView(ListView):
    model = Axle
    template_name = 'lists/list.html'
