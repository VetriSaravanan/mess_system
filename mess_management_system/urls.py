from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Include your app URLs here
    path('attendance/', include('attendance.urls')),
    path('meals/', include('meals.urls')),
    path('billing/', include('billing.urls')),
    path('notifications/', include('notifications.urls')),
    path('user/', include('homepage.urls')),  # Assuming 'user_homepage' is here
    path('students/', include('students.urls')),  # Students URL routing
    path('mess/', include('mess.urls')),  # Mess URL routing
    path('grocery/', include('grocery.urls')),

    # Add this to handle the root URL
    path('', lambda request: redirect('home')),  # Redirect to 'user_homepage'
]
