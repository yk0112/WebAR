import sys
from django.shortcuts import render
from .forms import AddImageForm, ImageSelectForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from .models import Image

# Create your views here.
def login(request):
   return render(request, 'WebAR/login')

def camera(request):
   return render(request, 'WebAR/camera.html')

@login_required(login_url='/admin/login')
def mb(request):
   if(request.method == 'POST'): 
      params = {
       'image': request.POST.get('image'),
       'size': request.POST.get('size'),
       'pattURL': request.POST.get('pattURL'),
      }
      return render(request, 'WebAR/camera.html', params)
   else:
      params = {
       'form': ImageSelectForm(request.user), 
      }         
      return render(request, 'WebAR/mb.html', params)

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
      'owner': request.user,
      'form': AddImageForm(instance=ins) 
   }   
   return render(request, 'WebAR/add.html', params)