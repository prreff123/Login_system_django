from django.shortcuts import render
from .models import User
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        name = User(email=email,password=password)
        name.save()
        return HttpResponse("<h1>User has been Added</h1>")
    else:
        return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')        