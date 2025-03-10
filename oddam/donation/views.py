from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
from django.views import View
from django.views.generic import TemplateView
from django.db.models import Sum
# from .forms import CustomUserCreationForm
from .forms import CustomUserCreationForm
from .models import Institution, Donation, Category
from django.core.paginator import Paginator



class LandingPageView(View):
    def get(self, request):
        bag_count = Donation.objects.aggregate(total_bags=Sum('quantity'))['total_bags'] or 0
        helped_org_count = Institution.objects.count()

        institutions_fund = Institution.objects.filter(type=Institution.FUNDACJA).order_by('id')
        institutions_org = Institution.objects.filter(type=Institution.ORGANIZACJA_POZARZADOWA).order_by('id')
        institutions_local = Institution.objects.filter(type=Institution.ZBIORKA_LOKALNA).order_by('id')

        paginator_fund = Paginator(institutions_fund, 5)
        page_fund = request.GET.get('page_fund')
        institutions_fund = paginator_fund.get_page(page_fund)

        paginator_org = Paginator(institutions_org, 5)
        page_org = request.GET.get('page_org')
        institutions_org = paginator_org.get_page(page_org)

        paginator_local = Paginator(institutions_local, 5)
        page_local = request.GET.get('page_local')
        institutions_local = paginator_local.get_page(page_local)

        context = {
            'bag_count': bag_count,
            'helped_org_count': helped_org_count,
            'institutions_fund': institutions_fund,
            'institutions_org': institutions_org,
            'institutions_local': institutions_local,
        }
        return render(request, "index.html", context)


class AddDonationView(View):
    def get(self, request):
        return render(request, "form.html")


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("landing_page")
        else:
            return redirect("register")


class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
        return render(request, "register.html", {"form": form})

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('landing_page')


# class UserLoginView(View):
#     def get(self, request):
#         return render(request, "login.html")
#
#     def post(self, request):
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         user = authenticate(request, username=email, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("landing_page")
#         return render(request, "login.html", {"error": "Nieprawidłowe dane logowania"})



# class RegisterView(View):
#     def get(self, request):
#         form = CustomUserCreationForm()
#         return render(request, "register.html", {"form": form})
#
#     def post(self, request):
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("landing_page")
#         return render(request, "register.html", {"form": form})
#
# class UserLoginView(View):
#     def get(self, request):
#         return render(request, "login.html")
#
#     def post(self, request):
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("landing_page")
#         return render(request, "login.html", {"error": "Nieprawidłowe dane logowania"})
