from django import forms
from .models import FaqQuestion


class FaqForm(forms.ModelForm):
    class Meta:
        model = FaqQuestion
        fields = '__all__'