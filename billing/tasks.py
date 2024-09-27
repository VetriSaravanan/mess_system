from billing.models import Bill
from attendance.models import Student
from django.utils import timezone

def generate_monthly_bills():
    """Generate bills for all students at the end of each month."""
    current_month = timezone.now().month
    students = Student.objects.all()

    for student in students:
        # Calculate the base total amount (e.g., meal cost * number of days in the month)
        days_in_month = 30  # You can adjust this dynamically based on the month
        meal_cost_per_day = student.daily_meal_cost
        total_amount = meal_cost_per_day * days_in_month

        # Create the bill instance
        bill = Bill.objects.create(student=student, total_amount=total_amount)

        # Apply the discount based on leave
        bill.apply_leave_discount(current_month)
