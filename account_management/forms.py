from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import gettext_lazy as _

from account_management.models import User, BaseUser


class CustomUserCreationForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(), required=False
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("Enter the same password as before, for verification."), required=False
    )

    class Meta:
        model = User
        fields = ("first_name", 'last_name', 'email',)


class CustomChangeUserForm(UserChangeForm):
    class Meta:
        model = BaseUser  # used with both admin and user
        fields = '__all__'

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"] if 'password' in self.initial else self.instance.password
