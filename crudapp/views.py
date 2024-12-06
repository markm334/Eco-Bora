from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm, FarmerRegistrationForm, CustomerRegistrationForm


def index(request):
    return render(request, 'index.html')
# Farmer Registration View
def farmer_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        farmer_form = FarmerRegistrationForm(request.POST)

        if user_form.is_valid() and farmer_form.is_valid():
            # Create user
            user = user_form.save()
            user.set_password(user.password)  # Set password securely
            user.save()

            # Create Farmer profile
            farmer = farmer_form.save(commit=False)
            farmer.user = user
            farmer.save()

            login(request, user)  # Log the user in immediately
            return redirect('farmer_dashboard')  # Redirect to the farmer's dashboard
    else:
        user_form = UserRegistrationForm()
        farmer_form = FarmerRegistrationForm()

    return render(request, 'farmer-register.html', {'user_form': user_form, 'farmer_form': farmer_form})

# Customer Registration View
def customer_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        customer_form = CustomerRegistrationForm(request.POST)

        if user_form.is_valid() and customer_form.is_valid():
            # Create user
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # Create Customer profile
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()

            login(request, user)  # Log the user in immediately
            return redirect('customer_dashboard')  # Redirect to the customer's dashboard
    else:
        user_form = UserRegistrationForm()
        customer_form = CustomerRegistrationForm()

    return render(request, 'customer-register.html', {'user_form': user_form, 'customer_form': customer_form})


def customer_dashboard(request):
    return None


def farmer_dashboard(request):
    return None