# homepage/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user_homepage, name='home'),  # 'home' should be here
]
