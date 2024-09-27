# accounts/backends.py
from django.contrib.auth.backends import ModelBackend
from .models import CustomUser
from django.db.models import Q

class CustomUserBackend(ModelBackend):
    """
    Custom authentication backend that allows users to log in using
    email, phone number, or username.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Try to login via email, phone, or username
            user = CustomUser.objects.get(
                Q(email=username) | Q(phone_number=username) | Q(username=username)
            )
        except CustomUser.DoesNotExist:
            return None
        
        # Check the password and return the user if valid
        if user.check_password(password):
            return user
        return None
