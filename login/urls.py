from django.urls import path
from .views import HelloWorld, UserList, BusinessProfileView

urlpatterns = [
    path('hello/', HelloWorld.as_view(), name='hello'),
    path('users/', UserList.as_view(), name='user-list'),
    path('business-profiles/', BusinessProfileView.as_view(), name='business-profile-list'),
  
]
