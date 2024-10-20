

# Create your models here.
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)  # Added phone number schema
    businessType = models.CharField(max_length=200)
    businessIndustry = models.CharField(max_length=200)
    onlineShop = models.BooleanField(default=False) 
    gst_in = models.CharField(max_length=15, unique=True)  # GST is typically alphanumeric in some regions (India: 15 digits)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username
    
    
class BusinessProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='business_profile')  # Keep user required
    business_name = models.CharField(max_length=255, blank=True, null=True)
    business_email = models.EmailField(unique=True, blank=True, null=True)
    business_phone = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    business_address = models.TextField(blank=True, null=True)
    business_website = models.URLField(blank=True, null=True)
    logo = models.URLField(blank=True, null=True)
    pinCode = models.CharField(max_length=10, blank=True, null=True)
    business_creation_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.business_name or 'No Business Name'} - {self.user.username}"


