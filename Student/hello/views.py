from django.shortcuts import render
from .models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,'login.html')

def preform_login(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed!")
    else:    
        username = request.POST.get("username")
        password = request.POST.get("password")
        name = authenticate(username=username,password=password)
        if name is not None:
            login(request, name)
            return HttpResponseRedirect(reverse("admin_dashboard"))
        else:
            return HttpResponseRedirect("/")

def admin_dashboard(request):
    return render(request,'admin_dashboard.html')        

def delete(request):
    logout(request)
    return HttpResponseRedirect("/")    