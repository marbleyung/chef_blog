from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('created_at', 'post', )
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Name'}),
                   'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
                   'website': forms.TextInput(attrs={'placeholder': 'Website'}),
                   'message': forms.Textarea(attrs={'placeholder': 'Your message'})}
