from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from datetime import timedelta
from .models import Attendance, Leave
from .forms import LeaveRequestForm
from .notification_util import send_notification  # If placed in a separate utility module

def attendance_list(request):
    filter_option = request.GET.get('filter', 'all')  # Get filter option from URL query parameter
    today = timezone.now().date()
    
    # Apply filter based on the option selected
    if filter_option == 'last_7_days':
        start_date = today - timedelta(days=7)
        attendance_records = Attendance.objects.filter(date__gte=start_date)
    elif filter_option == 'this_month':
        attendance_records = Attendance.objects.filter(date__year=today.year, date__month=today.month)
    else:
        attendance_records = Attendance.objects.all()  # Default: show all records
        
    return render(request, 'attendance/attendance_list.html', {'attendance_records': attendance_records})

def leave_list(request):
    filter_option = request.GET.get('filter', 'all')  # Get filter option from URL query parameter
    today = timezone.now().date()

    # Check if the user is a student and fetch the correct student instance
    if hasattr(request.user, 'student'):
        student = request.user.student  # Get the Student instance related to the logged-in user
        leaves = Leave.objects.filter(student=student)  # Query using the actual Student instance
    else:
        leaves = Leave.objects.all()  # For non-students, show all leave records

    # Apply filter based on the option selected
    if filter_option == 'last_7_days':
        start_date = today - timedelta(days=7)
        leaves = leaves.filter(start_date__gte=start_date)
    elif filter_option == 'this_month':
        leaves = leaves.filter(start_date__year=today.year, start_date__month=today.month)
    
    return render(request, 'attendance/leave_list.html', {'leave_records': leaves})


def send_notification(user, message):
    subject = "Notification"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]  # Assumes the user has an email field
    send_mail(subject, message, email_from, recipient_list)


def record_attendance(request):
    # Your logic to record attendance
    # After recording attendance, send the notification
    send_notification(request.user, "Your attendance has been recorded.")
    return render(request, 'attendance_records.html')


