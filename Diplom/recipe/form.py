from django import forms
from .models import Recipe


class FindName(forms.Form):
    name = forms.CharField(label='Название блюда', max_length=60)

class EntryName(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
