from django import forms
from .models import Farmer, Customer
from django.contrib.auth.models import User

# User Registration Form
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

# Farmer Registration Form
class FarmerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['location', 'product']

# Customer Registration Form
class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['address', 'preferred_product']
