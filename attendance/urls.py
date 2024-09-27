# attendance/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('attendance-list/', views.attendance_list, name='attendance_list'),
    path('leave-list/', views.leave_list, name='leave_list'),
]
