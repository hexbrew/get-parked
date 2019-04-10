from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import User
from .forms import CustomUserChangeForm

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    list_display = ('id','email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    ordering = ('-is_staff', 'email',)

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            return super(UserAdmin, self).get_form(request, obj, **kwargs)
        else:
            return CustomUserChangeForm
            