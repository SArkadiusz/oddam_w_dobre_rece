# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label="Adres e-mail",
        widget=forms.EmailInput(attrs={"placeholder": "Podaj e-mail"})
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]



# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ["username", "email", "password1", "password2"]

# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(
#         label="",
#         widget=forms.EmailInput(attrs={"placeholder": "Adres e-mail"})
#     )
#     name = forms.CharField(
#         label="",
#         widget=forms.TextInput(attrs={"placeholder": "Imię i nazwisko"})
#     )
#     password1 = forms.CharField(
#         label="",
#         widget=forms.PasswordInput(attrs={"placeholder": "Hasło"})
#     )
#     password2 = forms.CharField(
#         label="",
#         widget=forms.PasswordInput(attrs={"placeholder": "Powtórz hasło"})
#     )
#
#     class Meta:
#         model = CustomUser
#         fields = ["email", "name", "password1", "password2"]