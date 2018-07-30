from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser




class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['name', 'dp','cell','year','post']
    
    fieldsets = (
        (None, {'fields': ('name','password', 'dp','cell','year','post')}), )

admin.site.register(CustomUser, CustomUserAdmin)
