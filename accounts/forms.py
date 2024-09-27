from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

# Register Form: Used for user registration
class RegisterForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Phone number should contain only digits.')
        return phone_number

# Custom Authentication Form: Used for login
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Email/Phone/Registration Number')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('This field is required.')
        return username

# (Optional) If you plan to have a separate custom form for login
# This can be merged with CustomAuthenticationForm if desired
class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']

# Custom User Creation Form: Used by admin for creating users
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'role']  # Add more fields if required

    def clean_role(self):
        role = self.cleaned_data.get('role')
        if role not in [CustomUser.STUDENT, CustomUser.ADMIN, CustomUser.MESS_STAFF]:
            raise forms.ValidationError('Invalid role selection.')
        return role
