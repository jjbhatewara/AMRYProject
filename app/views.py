from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, auth, Group
from django.shortcuts import redirect, render, HttpResponse
from .forms import SatImageForm, UserRegisterForm
import cv2
import numpy as np
from .models import *
from django.contrib import messages
from AMRY import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.template import Context
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
    return render(request, 'signup.html', {'form': form, 'title':'reqister here'})

def Login(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        print("OK")
        user = authenticate(request, username = username, password = password)
        print("user")
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



@login_required
def index(req):
    if req.method == 'POST':
        form = SatImageForm(req.POST, req.FILES)
        # details = {}        
        # details['action'] = req.POST['action']
        # details['file_loc'] = 'media/images/'+ str(req.FILES['Sat_Main_Img'])
        if form.is_valid():
            form.save()
            act = req.POST['action']
            req.session['action'] = act
            req.session['file_loc'] = 'media/images/' + \
            str(req.FILES['Sat_Main_Img'])
            if int(act):
                return redirect('plane')
            else :
                return redirect('road')
    else:
        form = SatImageForm( initial={'action': '0'} )
    return render(req, 'index.html', {'form': form})


def success(req):
    print("suc")
    print(req.session.get('action'))
    return HttpResponse('successfully uploaded')


def plane(req):
    loc = req.session.get('file_loc')
    img = cv2.imread(loc)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,(102,73,145),(123,182,242))
    imask = mask>0
    green = np.zeros_like(img, np.uint8)
    green[imask] = img[imask]
    ## save  
    cnt = 0
    if SatImage.objects.exists():
        id1 = SatImage.objects.latest('id')
        cnt+=1
    cnt+=1
    Out_location = "media/Output/"+ str(cnt) + ".jpg"
    cv2.imwrite(Out_location,green)
    return render(req, 'plane.html', {'url': Out_location})


def road(req):
    return HttpResponse('road') 

