from django import forms
from .models import Joke

class JokeForm(forms.ModelForm):
    class Meta:
        model = Joke
        fields = ['content', 'author', 'category']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }