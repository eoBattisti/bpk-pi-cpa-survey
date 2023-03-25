from django import forms
from axis.models import Axle

class AxleForm(forms.ModelForm):

    class Meta:
        model = Axle
        fields = ['name', 'description']
        