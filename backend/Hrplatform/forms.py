from django import forms 
from .models import *

class AudioForm(forms.ModelForm):
    class Meta:
        model=Audio_store1
        fields=['video']