from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


from .forms import CustomUserCreationForm, CustomUserChange

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    form = CustomUserChange
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ('email', 'username',)

admin.site.register(CustomUser, CustomUserAdmin)


