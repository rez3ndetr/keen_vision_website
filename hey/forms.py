from django import forms

from .models import Registration, bid
from django.contrib.auth.forms import UserCreationForm


class UserForm(forms.ModelForm):
    class Meta:
        model = bid
        fields = "__all__"


class RegistrationUser(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"

# class RegistrationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = "__all__"