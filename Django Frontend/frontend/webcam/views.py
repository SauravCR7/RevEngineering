from django.shortcuts import render
from webcam.models import UploadForm,Upload
from django.http import HttpResponseRedirect
#from webcam.train1 import testmodel
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
import json
from django.views.decorators.csrf import csrf_exempt
import re
import base64
from webcam.lastfm_rec import nameinput
from webcam.facemood import detect
from webcam.movierec import get_recommendations,build_chart
from webcam.getmood import GetMood
from webcam.neural_style_transfer import nst 

text="Outside"

class HomePageView(TemplateView):
    template_name = "index.html"


def output1(request):
        #py_obj = 10
        py_obj=testmodel('F:/facial-frontend/frontend/media/'+uploaded_file_url)
        return render(request, 'output.html' ,{'output': py_obj})


def webcam(request):

    return render(request, 'webcam.html')

def about(request):
    if 'ArticleS' in request.POST:
        screenname = request.POST.get("Article", None)
        t=nameinput(screenname)
        print("------------------------------")
        print(t)
        t0=t[0]
        t1=t[1]
        t2=t[2]
        t3=t[3]
        t4=t[4]
        ll1=t[5]
        ll2=t[6]
        ll3=t[7]
        ll4=t[8]
        ll5=t[9]
        a0=t[10]
        a1=t[11]
        a2=t[12]
        a3=t[13]
        a4=t[14]

        return render(request, 'emotion.html' ,{'emo1': t0,'emo2': t1,'emo3': t2,'emo4': t3,'emo5': t4,'emo6': ll1,'emo7': ll2,'emo8': ll3,'emo9': ll4,'emo10': ll5,'emo11': a0,'emo12': a1,'emo13': a2,'emo14': a3,'emo15': a4,})

   

    if 'KeyWordS' in request.POST:
        screenname1 = request.POST.get("KeyWord", None)
        k=get_recommendations(screenname1)
        t0=k[0]
        t1=k[1]
        t2=k[2]
        t3=k[3]
        t4=k[4]

        return render(request, 'emotion1.html',{'emo1': t0,'emo2': t1,'emo3': t2,'emo4': t3,'emo5': t4})

    return render(request,'about.html')



@csrf_exempt
def imgdata(request):
    if request.is_ajax():
        url = request.POST.get('image_data')
        print("Received!!!!!")
        text="inside"

        with open('D:/Machine Learning/Dirty/RevEngineering/Django Frontend/frontend/media/webcam/webcam.png', 'wb') as f:
            f.write(base64.decodestring(url.split(',')[1].encode()))
        return render(request, 'index.html')
    return render(request,'output.html',{'output':'Not Received'})


def emotion(request):
    text="Hey! I'm inside!"
    return render(request,'index0.html')





def textinput(request):
    if 'ArticleS' in request.POST:
        screenname = request.POST.get("Article", None)
        t=GetMood(screenname)
        if t==0:    
            nst(0)
            x = "You Seem Unhappy. Here is an Image of you in a Radiant Style!"
        else:
            nst(1)
            x = "You Seem Happy. Here is an Image of you in a Solemn Style!"
        return render(request,'output.html',{'output':t})

    return render(request,'textinput.html')

def imgpredict(request):
    
    pred=detect("D:/Machine Learning/Dirty/RevEngineering/Django Frontend/frontend/media/webcam/webcam.png")
    if pred==0:
        nst(0)
        text="You are Sad :("
    else:
        nst(1)
        text="Such a jolly person you are!"
    return render(request,'output.html',{'output': text})


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = (filename)
        print(uploaded_file_url)
        pred=detect("D:/Machine Learning/Dirty/RevEngineering/Django Frontend/frontend/media/"+uploaded_file_url)
        #py_obj=testmodel('media/'+uploaded_file_url)
        return render(request, 'output.html' ,{'output': pred})

    return render(request, 'simple_upload.html')
