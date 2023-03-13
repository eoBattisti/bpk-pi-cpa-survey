"""Middlewares for the BPK Search Project."""

from django.utils import translation


class UserLanguageMiddleware:
    """User language middleware."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        translation.activate('pt-br')
        return self.get_response(request)
