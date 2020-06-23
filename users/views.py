from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "users/user.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "users/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {"message": "Logged out."})

def register_view(request):
        return render(request, "users/register.html",{"message":"Create an account!"})


def register(request):
    username=request.POST.get("username")
    email=request.POST.get("email")
    password1=request.POST.get("password1")
    password2=request.POST.get("password2")
    if User.objects.filter(username=username).count()!=0:
        return render(request, "users/register.html",{"message":"Username taken please try another username!"})
    elif password1==password2:
        user=User.objects.create_user(username,email=email,password=password1)
        user.save()
        return render(request, "users/login.html",{"message":"Successfully created! Please login now!"})
    else:
        return render(request, "users/register.html",{"message":"Passwords do not match!"})
