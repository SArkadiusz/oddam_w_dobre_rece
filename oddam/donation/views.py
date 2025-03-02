from django.shortcuts import render

def landing_page(request):
    return render(request, "index.html")

def add_donation(request):
    return render(request, "form.html")

def login_view(request):
    return render(request, "login.html")

def register_view(request):
    return render(request, "register.html")
