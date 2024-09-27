# billing/utils.py
from attendance.models import Attendance, Leave
from meals.models import MealPlan
from datetime import timedelta

def calculate_bill_for_student(student):
    total_amount = 0
    today = timezone.now().date()
    meal_plans = MealPlan.objects.filter(date__lte=today)  # Get past meal plans up to today

    for meal_plan in meal_plans:
        attendance = Attendance.objects.filter(student=student, date=meal_plan.date).first()
        if attendance and attendance.is_eligible_for_billing():
            total_amount += meal_plan.cost_per_day

    # Factor in leave discounts or exclusions
    leaves = Leave.objects.filter(student=student)
    for leave in leaves:
        for meal_plan in meal_plans:
            if leave.is_on_leave(meal_plan.date):
                total_amount -= meal_plan.cost_per_day  # Adjust the bill for the leave days

    return total_amount
