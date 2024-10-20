from rest_framework import serializers
from .models import User , BusinessProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'businessType', 'businessIndustry', 'onlineShop', 'gst_in']

    def validate(self, data):
        # Ensure either email or phone number is provided
        if not data.get('email') and not data.get('phone_number'):
            raise serializers.ValidationError("At least one of 'email' or 'phone number' must be provided.")
        
        # Validate required fields (email, phone_number are already covered)
        required_fields = ['username', 'businessType', 'businessIndustry']
        for field in required_fields:
            if not data.get(field):
                raise serializers.ValidationError(f"'{field}' is required.")
        
        # GSTIN is optional, so no validation needed for it unless specific rules apply
        return data
    
    
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
        

    