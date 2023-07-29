import sys
import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from .forms import AddImageForm, ImageSelectForm
from .models import Image




def camera_mb(request):
    return render(request, "WebAR/camera_mb.html")


def camera_lb(request):
    return render(request, "WebAR/camera_lb.html")


@login_required(login_url="/")
def mb(request):
    if request.method == "POST":
        if request.POST.get("patt") == "":
            messages.add_message(request, messages.ERROR, "Please select a marker")
            return redirect(to="./markerbase")
        else:
            f = open("WebAR/static/WebAR/marker.patt", "w")
            f.write(request.POST.get("patt"))
            image = request.POST.get("image1")
            scale = request.POST.get("size")
            target = Image.objects.filter(image=image)
            size = str(float(target[0].size) * float(scale))
            params = {
                "username": request.user.username,
                "image": image,
                "size": size,
            }
            return render(request, "WebAR/camera_mb.html", params)
    else:
        params = {
            "username": request.user.username,
            "form": ImageSelectForm(request.user),
        }
        return render(request, "WebAR/mb.html", params)


@login_required(login_url="/")
def lb(request):
    if request.method == "POST":
        if request.POST.get("latitude") == "":
            messages.add_message(
                request, messages.ERROR, "Please enter a latitude value"
            )
            return redirect(to="./locationbase")

        elif request.POST.get("longitude") == "":
            messages.add_message(
                request, messages.ERROR, "Please enter a longitude value"
            )
            return redirect(to="./locationbase")
        else:
            image = request.POST.get("image1")
            scale = request.POST.get("size")
            target = Image.objects.filter(image=image)
            size = str(float(target[0].size) * float(scale))
            params = {
                "image": image,
                "latitude": request.POST.get("latitude"),
                "longitude": request.POST.get("longitude"),
                "size": size,
            }
            return render(request, "WebAR/camera_lb.html", params)
    else:
        params = {
            "username": request.user.username,
            "form": ImageSelectForm(request.user),
            "API_KEY": "apikey",
        }
        return render(request, "WebAR/lb.html", params)

@login_required(login_url="/")
def face(request):
    if request.method == "POST":
        Itemcount = int(request.POST.get("item_count"))
        form_list = []
        for i in range(Itemcount):
            index = i
            image = request.POST.get("image" + str(i + 1))
            anchor = request.POST.get("item" + str(i + 1) + "_anchor")
            rotateX = request.POST.get("item" + str(i + 1) + "_rotateX")
            rotateY = request.POST.get("item" + str(i + 1) + "_rotateY")
            rotateZ = request.POST.get("item" + str(i + 1) + "_rotateZ")
            positionX = request.POST.get("item" + str(i + 1) + "_positionX")
            positionY = request.POST.get("item" + str(i + 1) + "_positionY")
            positionZ = request.POST.get("item" + str(i + 1) + "_positionZ")
            scale = request.POST.get("item" + str(i + 1) + "_scale")
            target = Image.objects.filter(image=image)
            nickname = target[0].nickname
            size = str(float(target[0].size) * float(scale))
            if i < Itemcount and not (
                str.isdigit(rotateX)
                and str.isdigit(rotateY)
                and str.isdigit(rotateZ)
                and str.isdigit(anchor)
            ):
                messages.add_message(
                    request, messages.ERROR, "Enter a number for Rotation"
                )
                return redirect(to="./face")
            form_list.append(
                {
                    "index": index,
                    "image": image,
                    "anchor": anchor,
                    "rotateX": rotateX,
                    "rotateY": rotateY,
                    "rotateZ": rotateZ,
                    "positionX": positionX,
                    "positionY": positionY,
                    "positionZ": positionZ,
                    "scale": size,
                    "nickname": nickname,
                }
            )
        params = {"form_list": form_list, "count": Itemcount}
        return render(request, "WebAR/camera_face.html", params)
    else:
        params = {
            "username": request.user.username,
            "form": ImageSelectForm(request.user),
        }
        return render(request, "WebAR/face.html", params)


@login_required(login_url="/")
def add(request):
    ins = Image(owner=request.user)
    if request.method == "POST":
        ImageForm = AddImageForm(request.POST, request.FILES, instance=ins)
        if ImageForm.is_valid():
            messages.add_message(
                request, messages.SUCCESS, "Your registration is complete!"
            )
            ImageForm.save()
            return redirect(to="./add")
        else:
            messages.add_message(
                request, messages.ERROR, "Your registration is failed."
            )
            return redirect(to="./add")
    params = {
        "username": request.user.username,
        "owner": request.user,
        "form": AddImageForm(instance=ins),
    }
    return render(request, "WebAR/add.html", params)


@login_required(login_url="/")
def delete(request):
    if request.method == "POST":
        imgName = request.POST.get("image1")
        Image.objects.filter(image=imgName).delete()
        messages.add_message(request, messages.SUCCESS, "Deletion completed!")
        return redirect(to="./delete")
    params = {
        "username": request.user.username,
        "owner": request.user,
        "form": ImageSelectForm(request.user),
    }
    return render(request, "WebAR/delete.html", params)
