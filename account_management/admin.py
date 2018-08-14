from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from account_management.permissions import AllowOnlyCreatorToChangeDeleteUser, \
    AllowOnlyCreatorIBAN
from core.permission import ExtraObjectLevelPermission
from .forms import CustomUserCreationForm, CustomChangeUserForm
from .models import User, BankAccount, Admin


class BankAccountInline(ExtraObjectLevelPermission, admin.TabularInline):
    model = BankAccount
    permission_class = AllowOnlyCreatorToChangeDeleteUser


class CustomUser(ExtraObjectLevelPermission, UserAdmin):
    inlines = (BankAccountInline,)
    add_form = CustomUserCreationForm
    form = CustomChangeUserForm
    permission_class = AllowOnlyCreatorToChangeDeleteUser

    list_display = ('email', 'first_name', 'last_name', 'created_by',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2',),
        }),
    )
    ordering = ('email',)

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


class CustomAdmin(UserAdmin):
    form = CustomChangeUserForm

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2',),
        }),
    )
    ordering = ('email',)


class BankAccountAdmin(ExtraObjectLevelPermission, admin.ModelAdmin):
    list_display = ('iban', 'owner', 'status')
    permission_class = AllowOnlyCreatorIBAN

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['owner'].queryset = User.objects.filter(
            created_by=request.user)  # retrieve only user that created by admin
        return form


admin.site.register(User, CustomUser)
admin.site.register(Admin, CustomAdmin)
admin.site.register(BankAccount, BankAccountAdmin)
