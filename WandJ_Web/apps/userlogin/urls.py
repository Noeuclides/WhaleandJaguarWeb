"""WandJ_Web userlogin App URL Configuration
"""
from django.urls import path, include
from .views import SignUp, Home


urlpatterns = [
    path('signup/', SignUp, name='signup'),
    path('', Home, name='home'),
    path('', include('django.contrib.auth.urls')),
]
