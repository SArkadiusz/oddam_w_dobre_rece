from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm

def landing_page(request):
    return render(request, "index.html")

def add_donation(request):
    return render(request, "form.html")

def login_view(request):
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("landing_page")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("landing_page")
        else:
            return render(request, "login.html", {"error": "Nieprawidłowe dane logowania"})

    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("landing_page")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("landing_page")
        else:
            return render(request, "login.html", {"error": "Nieprawidłowe dane logowania"})

    return render(request, "login.html")