
# forms.py


from django import forms
from django.forms import widgets
from .models import *

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper



class SatImageForm(forms.ModelForm):

    class Meta:
        model = SatImage
        fields = ['Sat_Main_Img','action']
        widgets = { 
            'action': forms.RadioSelect(attrs={'class': "custom-radio-list"})
        }

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 
    class Meta:
        model = User
        fields = ['username','password1', 'password2']

    

    
        

