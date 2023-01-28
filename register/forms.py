from django import forms

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

# One Form = One Class

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User    # refers to the Users table in the database
        fields = ["username", "email", "password1", "password2"]    # sequence of how the input fields will show up

