
# forms.py


from django import forms
from django.forms import widgets
from .models import *

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper



class SatImageForm(forms.ModelForm):


    # def get_form_kwargs(self):
    #     """
    #     Returns the keyword arguments for instanciating the form.
    #     """
    #     kwargs = {'initial': self.get_initial()}
    #     if self.request.method in ('POST', 'PUT'):
    #         kwargs.update({
    #             'data': self.request.POST,
    #             'files': self.request.FILES,
    #             'request': self.request})
    #     return kwargs
    class Meta:
        model = SatImage
        fields = ['Sat_Main_Img','action']
        widgets = { 
            'action': forms.RadioSelect(attrs={'class': "custom-radio-list"})
        }
    # def __init__(self, *args, **kwargs):
    #    self.request = kwargs.pop('request', None)
    #    return super().__init__(*args, **kwargs) 

    # def save(self, *args, **kwargs):
    #    kwargs['commit']=False
    #    obj = super().save(*args, **kwargs)
    #    if self.request:
    #        obj.user = self.request.user
    #    obj.save()
    #    return obj
    def save(self, user):
        obj = super().save(commit = False)
        obj.created_by = user
        obj.save()
        return obj
    # def save_model(self, request, obj, form, change):
    #     if not change:
    #         obj.creator = request.user
    #     obj.save()

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

    

    
        

