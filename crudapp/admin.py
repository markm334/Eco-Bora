# Import the correct models from your models.py
from django.contrib import admin
from .models import Farmer, Customer  # Corrected import

# Register Farmer and Customer models in Django admin
admin.site.register(Farmer)
admin.site.register(Customer)
