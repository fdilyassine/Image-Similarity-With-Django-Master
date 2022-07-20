# posts/forms.py
from django import forms
from .models import Vector

class PostForm(forms.ModelForm):

    class Meta:
        model = Vector
        fields = ['vector']