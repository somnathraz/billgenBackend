from rest_framework import serializers
from .models import User , BusinessProfile
import random
import string

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'businessType', 'businessIndustry', 'onlineShop', 'gst_in']

    def validate(self, data):
        # Ensure either email or phone number is provided
        if not data.get('email') and not data.get('phone_number'):
            raise serializers.ValidationError("At least one of 'email' or 'phone number' must be provided.")
        # Check for existing users with the same email or phone number
        if User.objects.filter(email=data.get('email')).exists():
            raise serializers.ValidationError({"email": "A user with this email already exists."})

        if User.objects.filter(phone_number=data.get('phone_number')).exists():
            raise serializers.ValidationError({"phone_number": "A user with this phone number already exists."})

        return data
    
     
    def create(self, validated_data):
        # Generate a random username if not provided
        if 'username' not in validated_data or not validated_data['username']:
            validated_data['username'] = self.generate_random_username()
        return super().create(validated_data)

    @staticmethod
    def generate_random_username(length=8):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    
    
    
    
class BusinessProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProfile
        fields = [
            'business_name',
            'business_email',
            'business_phone',
            'state',
            'business_address',
            'business_website',
            'logo',
            'pinCode',
            'business_creation_date'
        ]
    
    # Custom validation for business_phone
    def validate_business_phone(self, value):
        if len(value) != 10:
            raise serializers.ValidationError("Phone number must be 10 digits.")
        return value
        

    