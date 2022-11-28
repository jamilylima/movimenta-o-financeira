from django import forms
from .models import Dados

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Dados
        fields = ["file"]
