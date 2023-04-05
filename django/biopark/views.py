"""Biopark views for Biopark Search project."""
from django.views.generic import TemplateView, RedirectView
from django.http import Http404
from django.shortcuts import render

class HomeView(RedirectView):
    """
    Home page
    """
    def get_redirect_url(self, *args, **kwargs):
        """
        Redirect users to correct home page.
        """

        raise Http404


class Handler400View(TemplateView):
    """
    Handler 400 view.
    """
    template_name = 'handler/400.html'


class Handler404View(TemplateView):
    """
    Handler 404 view.
    """
    template_name = 'handler/404.html'


class Handler500View(TemplateView):
    """
    Handler 500 view.
    """
    template_name = 'handler/500.html'


class Handler403View(TemplateView):
    """
    Handler 403 view.
    """
    template_name = 'handler/403.html'

