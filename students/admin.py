from django.contrib import admin
from .models import Student, Attendance, Bill

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user']

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'date', 'status']

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['student', 'amount', 'date_issued', 'is_paid']
