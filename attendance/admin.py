# attendance/admin.py
from django.contrib import admin
from .models import Attendance, Leave

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'consumed_meal')
    list_filter = ('date', 'consumed_meal')
    search_fields = ('student__name',)


@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ('student', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('student__name',)
