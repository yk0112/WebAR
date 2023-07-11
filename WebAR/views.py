import sys
import json
from myapp.local_settings import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from .forms import AddImageForm, ImageSelectForm
from .models import Image

# Create your views here.
def login(request):
   return render(request, 'WebAR/login')

def camera_mb(request):
   return render(request, 'WebAR/camera_mb.html')

def camera_lb(request):
   return render(request, 'WebAR/camera_lb.html')

@login_required(login_url='/admin/login')
def mb(request):
   if(request.method == 'POST'): 
      if(request.POST.get('patt') == ""):
         messages.add_message(request, messages.ERROR, "マーカーを選択してください")
         return redirect(to='./markerbase')
      else:
        f = open('WebAR/static/WebAR/marker.patt', 'w')
        f.write(request.POST.get('patt'))
        params = {
         'username': request.user.username, 
         'image': request.POST.get('image'),
         'size': request.POST.get('size'),
        }
        return render(request, 'WebAR/camera_face.html', params)
   else:
      params = {
       'username': request.user.username, 
       'form': ImageSelectForm(request.user), 
      }         
      return render(request, 'WebAR/mb.html', params)

@login_required(login_url='/admin/login')
def lb(request):      
   if(request.method == 'POST'):
      if(request.POST.get('latitude') == ""):
         messages.add_message(request, messages.ERROR, "緯度を入力してください")
         return redirect(to='./locationbase')
      
      elif(request.POST.get('longitude') == ""):
         messages.add_message(request, messages.ERROR, "経度を入力してください")
         return redirect(to='./locationbase')
      else:
        params = {
         'image': request.POST.get('image'),
         'latitude': request.POST.get('latitude'), 
         'longitude': request.POST.get('longitude'),
         'size': request.POST.get('size'),
        }
        return render(request, 'WebAR/camera_lb.html', params)
   else:
      params = {
       'username': request.user.username, 
       'form': ImageSelectForm(request.user), 
       'API_KEY': GOOGLEMAP_API_KEY
      }         
      return render(request, 'WebAR/lb.html', params)
   

@login_required(login_url='/admin/login')
def face(request):    
   params = {
       'username': request.user.username, 
       'form1': ImageSelectForm(request.user), 
       'form2': ImageSelectForm(request.user), 
       'form3': ImageSelectForm(request.user), 
       'form4': ImageSelectForm(request.user), 
       'form5': ImageSelectForm(request.user), 
      }   
   return render(request, 'WebAR/face.html', params);   


@login_required(login_url='/admin/login')
def add(request):
   ins = Image(owner=request.user)
   if request.method == 'POST':
      ImageForm = AddImageForm(request.POST,request.FILES,instance=ins)
      if ImageForm.is_valid():
         messages.add_message(request, messages.SUCCESS, "登録完了しました！")
         ImageForm.save()
         return redirect(to='./add')
      else:
         messages.add_message(request, messages.ERROR, "登録に失敗しました")
         return redirect(to='./add')
   params = {
      'username': request.user.username, 
      'owner': request.user,
      'form': AddImageForm(instance=ins) 
   }   
   return render(request, 'WebAR/add.html', params)

@login_required(login_url='/admin/login')
def delete(request):
   if(request.method == 'POST'):
      imgName = request.POST.get('image')
      print(imgName)
      Image.objects.filter(image=imgName).delete()
      messages.add_message(request, messages.SUCCESS, "削除しました!")
      return redirect(to='./delete')
   params = {
      'username': request.user.username, 
      'owner': request.user,
      'form': ImageSelectForm(request.user), 
   }   
   return render(request, 'WebAR/delete.html', params)