from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from .models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        help_text=_("Required. Please enter a valid email address."),
    )

    class Meta:
        model = User
        fields = ("email", "password1", "password2")
