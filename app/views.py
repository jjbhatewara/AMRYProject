from django.shortcuts import redirect, render, HttpResponse
from .forms import SatImageForm
import cv2
import numpy as np
from .models import *
# Create your views here.


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

