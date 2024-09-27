from decimal import Decimal
from django.db import models
from accounts.models import Student
from django.utils import timezone
import calendar

class Leave(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='billing_leaves')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Leave for {self.student.user.username} from {self.start_date} to {self.end_date}"


class Bill(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    date_generated = models.DateField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Bill for {self.student.user.username} - Total: {self.total_amount} Final: {self.final_amount}"

    def calculate_total(self):
        """Calculate the total amount after applying the discount."""
        return self.total_amount - self.discount

    @property
    def final_amount(self):
        """Dynamically calculate the final amount with the discount."""
        return self.calculate_total()

    def apply_leave_discount(self, month):
        """Apply discount if the student has continuous 7, 14, 21, or 28-day leave."""
        current_year = timezone.now().year

        # Determine the first and last day of the specified month
        try:
            month_start = timezone.now().replace(month=month, day=1).date()
            last_day = calendar.monthrange(current_year, month)[1]
            month_end = timezone.now().replace(month=month, day=last_day).date()
        except ValueError as e:
            print(f"Invalid month provided: {month}. Error: {e}")
            return

        # Filter leaves that overlap with the given month
        leaves = Leave.objects.filter(
            student=self.student,
            start_date__lte=month_end,  # Leave starts on or before the end of the month
            end_date__gte=month_start   # Leave ends on or after the start of the month
        )

        total_discount = Decimal('0.00')
        meal_cost_per_day = Decimal(self.student.daily_meal_cost)  # Ensure it's Decimal

        if not leaves.exists():
            print(f"No leaves found for {self.student.user.username} in month {month}.")

        for leave in leaves:
            # Calculate the total number of leave days
            leave_duration = (leave.end_date - leave.start_date).days + 1

            # Calculate the number of discountable days based on multiples of 7
            if leave_duration >= 7:
                discount_days = (leave_duration // 7) * 5  # 5 days discount for every 7 days of leave
                discount_amount = meal_cost_per_day * Decimal(discount_days)
                total_discount += discount_amount

                # Debugging Information
                print(f"Leave detected: {leave_duration} days from {leave.start_date} to {leave.end_date}")
                print(f"Applying discount: {discount_amount} (for {discount_days} discount days)")

        self.discount = total_discount
        self.save()

        # Log the total discount applied
        print(f"Total discount applied: {self.discount}")
