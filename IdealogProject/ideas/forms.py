from django import forms
from .models import Idea

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        # include fields (tags exists in migrations so include it)
        fields = ['title', 'description', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-lg shadow-sm rounded-pill',
                'placeholder': 'Enter your idea title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control form-control-lg shadow-sm rounded-3',
                'placeholder': 'Describe your idea',
                'rows': 6,
                'maxlength': '1200'
            }),
            'tags': forms.TextInput(attrs={
                'class': 'form-control form-control-lg shadow-sm rounded-pill',
                'placeholder': 'Add tags separated by commas'
            }),
        }
