from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Institution(models.Model):
    FUNDACJA = "fundacja"
    ORGANIZACJA_POZARZADOWA = "organizacja"
    ZBIORKA_LOKALNA = "zbiórka"

    INSTITUTION_TYPES = [
        (FUNDACJA, "Fundacja"),
        (ORGANIZACJA_POZARZADOWA, "Organizacja pozarządowa"),
        (ZBIORKA_LOKALNA, "Zbiórka lokalna"),
    ]

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=INSTITUTION_TYPES, default=FUNDACJA)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.PositiveIntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Dar {self.quantity} worków dla {self.institution.name}"