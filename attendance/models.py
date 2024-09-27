from django.db import models
from accounts.models import Student
from datetime import timedelta

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    consumed_meal = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.student.name} - {self.date}"

    def is_eligible_for_billing(self):
        """Check if the student is eligible for billing on this date."""
        return self.consumed_meal


class Leave(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_leaves')  # Unique related_name
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Leave for {self.student.user.username} from {self.start_date} to {self.end_date}"


    def is_on_leave(self, date):
        """Check if the student is on leave on a particular date."""
        return self.start_date <= date <= self.end_date

    def is_continuous_seven_day_leave(self):
        """Check if the leave period is exactly 7, 14, 21, or 28 days long."""
        days_off = (self.end_date - self.start_date).days + 1
        return days_off in [7, 14, 21, 28]
