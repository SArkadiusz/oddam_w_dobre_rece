from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Institution
# Register your models here.

admin.site.register(User, UserAdmin)

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "description")
    search_fields = ("name", "description")
    list_filter = ("type",)
    ordering = ("name",)