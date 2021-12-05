import os
import sys

import cv2
import numpy as np
from AMRY import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group, User, auth
from django.shortcuts import HttpResponse, redirect, render
from django.template import Context
from django.template.loader import get_template

from .forms import SatImageForm, UserRegisterForm
from .models import *
from .Roads.roads import Roads

# sys.path.append('../yolov5/')


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, f'Your account has been created ! You are now able to log in')            
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form, 'title':'reister here'})

def Login(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        # print("OK")
        user = authenticate(request, username = username, password = password)
        # print("user")
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('home')
        else:
            messages.info(request,'Invalid Username or Password')
    form = AuthenticationForm()
    form.fields['username'].widget.attrs['class'] = "form-control form-control-lg"
    form.fields['username'].widget.attrs['placeholder'] = "Username"
    form.fields['username'].widget.attrs['id'] = "Username"
    form.fields['password'].widget.attrs['class'] = "form-control form-control-lg"
    form.fields['password'].widget.attrs['placeholder'] = "password"
    form.fields['password'].widget.attrs['id'] = "typePasswordX" 
    return render(request, 'login.html', {'form':form, 'title':'log in'})

def logout(request):
    """Logout Function for all users."""
    auth.logout(request)
    return redirect('/')

@login_required
def index(req):
    # print(req.user)
    if req.method == 'POST':
        form = SatImageForm(req.POST,req.FILES)
        # print(form)
        # form.created_by = req.user
        # print(form.created_by)
        # details = {}        
        # details['action'] = req.POST['action']
        # details['file_loc'] = 'media/images/'+ str(req.FILES['Sat_Main_Img'])
        if form.is_valid():
            obj = form.save(req.user)
            # print(obj.Sat_Main_Img)
            act = req.POST['action']
            req.session['action'] = act
            req.session['file_loc'] = str (obj.Sat_Main_Img)
            # req.session['file_loc'] = 'media/images/' + \
            # str(req.FILES['Sat_Main_Img'])
            temp_sel = int(act)
            if temp_sel == 1:
                return redirect('plane')
            elif temp_sel == 0 :
                return redirect('road')
            else:
                return redirect('building')

    else:
        form = SatImageForm( initial={'action': '0'} )
    return render(req, 'index.html', {'form': form})

@login_required
def success(req):
    print("suc")
    print(req.session.get('action'))
    return HttpResponse('successfully uploaded')

@login_required
def plane(req):
    loc = req.session.get('file_loc')
    inp_loc = "media/" + loc
    temp = loc.split("/")
    para = "python ../yolov5/detect.py --weights ../yolov5/best.pt --img 416 --conf 0.4 --imgname "+ temp[-1] +" --source " + inp_loc
    # para = "python ../yolov5/detect.py  --source 0" 
    print("RUNNING YOLOv5")
    os.system(para)
    loc = "media/Output/" + temp[-1]
    return render(req, 'plane.html', {'url': loc})

@login_required
def road(req):
    
    loc = req.session.get('file_loc')
    inp_loc = "media/" + loc
    Roads(inp_loc)
    return HttpResponse('road') 

@login_required
def building(req):
    
    loc = req.session.get('file_loc')
    inp_loc = "media/" + loc
    Roads(inp_loc)
    return HttpResponse('road') 