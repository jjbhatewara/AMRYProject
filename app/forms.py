
# forms.py
from django import forms
from .models import *


class SatImageForm(forms.ModelForm):

    class Meta:
        model = SatImage
        fields = ['Sat_Main_Img','action']
        widgets = { 
            'action': forms.RadioSelect(attrs={'class': "custom-radio-list"})
        }

