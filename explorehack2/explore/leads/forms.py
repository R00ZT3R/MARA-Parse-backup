from django import forms

from .models import TextInput

class TextForm(forms.ModelForm):
    class Meta:
        model=TextInput
        fields=["textInput"]