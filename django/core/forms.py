from django import forms
from django.core.exceptions import ValidationError


class ImportForm(forms.Form):

    allowed_types = []
    file = forms.FileField()

    def __init__(self, types, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allowed_types = types

    def clean(self):
        file = self.cleaned_data.get('file')
        extension = file.name.split('.')[-1]
        print(self.allowed_types)
        if extension not in self.allowed_types:
            raise ValidationError(
                {'file': 'Arquivo inválido para importação'}
            )
