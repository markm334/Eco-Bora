from django.db import models
from django.contrib.auth.models import User

# Farmer Model
class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to the User model
    location = models.CharField(max_length=255)
    product = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

# Customer Model
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to the User model
    address = models.CharField(max_length=255)
    preferred_product = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
