from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User, BusinessProfile
from .serializers import UserSerializer, BusinessProfileSerializer
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.models import User
from django.http import HttpResponse

class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello from Django backend!"})

class UserList(APIView):
    @swagger_auto_schema(
        responses={200: UserSerializer(many=True)},  # Documenting the response for GET
    )
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={201: UserSerializer(), 400: 'Bad Request'},  # Documenting the response for POST
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        print(serializer.is_valid(),"from check")
        if serializer.is_valid():
             # Check if a user with the same email or phone number exists
            if User.objects.filter(email=serializer.validated_data.get('email')).exists():
                return Response({'detail': 'User with this email already exists.'}, status=status.HTTP_409_CONFLICT)

            if User.objects.filter(phone_number=serializer.validated_data.get('phone_number')).exists():
                return Response({'detail': 'User with this phone number already exists.'}, status=status.HTTP_409_CONFLICT)

            serializer.save()  # Automatically triggers BusinessProfile creation via signal
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # Check for duplicate email or phone number errors
      
        
        if 'phone_number' in serializer.errors:
            if serializer.errors['phone_number'][0].code == 'unique':
                return Response(
                    {'detail': 'User with this phone number already exists.'}, 
                    status=status.HTTP_409_CONFLICT
                )

        if 'email' in serializer.errors:
            if serializer.errors['email'][0].code == 'unique':
                return Response(
                    {'detail': 'User with this email already exists.'}, 
                    status=status.HTTP_409_CONFLICT
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    
class BusinessProfileView(APIView):
    @swagger_auto_schema(
        responses={200: BusinessProfileSerializer(many=True)},  # Documenting the response for GET
    )
    def get(self, request):
        business_profile = BusinessProfile.objects.all()
        serializer = BusinessProfileSerializer(users, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=BusinessProfileSerializer,
        responses={201: BusinessProfileSerializer(), 400: 'Bad Request'},  # Documenting the response for POST
    )
    def post(self, request):
        serializer = BusinessProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

