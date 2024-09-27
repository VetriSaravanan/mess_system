# homepage/views.py (or in your existing app's views.py)

from django.shortcuts import render


def user_homepage(request):
    return render(request, 'homepage/home.html')  # Ensure this template exists

    
    # homepage/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world!")

