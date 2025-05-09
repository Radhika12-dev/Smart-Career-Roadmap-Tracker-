from django.urls import path
from .views import *

urlpatterns = [
    
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name="profile")
]
