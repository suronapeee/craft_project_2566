from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # new
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm # new
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)

