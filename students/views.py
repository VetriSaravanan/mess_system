from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from .models import Student, Attendance, Bill

@login_required
def student_dashboard(request):
    # Try to get the Student instance related to the current user
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        # If no student record is found, show a 404 error
        return HttpResponseNotFound('No student record found for this user.')
    
    # Fetch the last 10 attendance records for the current student
    attendance_history = Attendance.objects.filter(student=student).order_by('-date')[:10]
    
    # Fetch the next 5 pending bills for the current student
    upcoming_bills = Bill.objects.filter(student=student, is_paid=False).order_by('date_issued')[:5]

    # Render the template with the fetched data
    context = {
        'attendance_history': attendance_history,
        'upcoming_bills': upcoming_bills
    }
    
    return render(request, 'students/student_dashboard.html', context)
