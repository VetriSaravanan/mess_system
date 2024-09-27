from django.test import TestCase
from .models import Bill, Student, Leave
from accounts.models import CustomUser
from decimal import Decimal
from django.utils import timezone
from datetime import timedelta

class BillModelTest(TestCase):

    def setUp(self):
        # Create a mock user
        self.user = CustomUser.objects.create_user(username='testuser', password='password123')
        
        # Create a mock student linked to the created user
        self.student = Student.objects.create(
            user=self.user,
            registration_number='REG123',
            hostel_status=True,
            daily_meal_cost=Decimal('100.00')
        )
        
        # Create a mock bill
        self.bill = Bill.objects.create(
            student=self.student,
            total_amount=Decimal('3000.00')
        )

    def create_leave(self, days, start_date=None, end_date=None):
        """Helper method to create continuous leave for 'days' days."""
        if not end_date:
            end_date = timezone.now().date()
        if not start_date:
            start_date = end_date - timedelta(days=days - 1)
        return Leave.objects.create(student=self.student, start_date=start_date, end_date=end_date)

    def test_bill_calculate_total(self):
        """Test that the bill total amount calculation works correctly."""
        self.assertEqual(self.bill.calculate_total(), Decimal('3000.00'))

    def test_bill_str_method(self):
        """Test the string representation of the bill."""
        expected_str = f"Bill for {self.bill.student.user.username} - Total: {self.bill.total_amount} Final: {self.bill.final_amount}"
        self.assertEqual(str(self.bill), expected_str)

    def test_discount_for_7_day_leave(self):
        """Test discount application for a 7-day continuous leave."""
        self.create_leave(7)
        self.bill.apply_leave_discount(timezone.now().month)
        
        # 5 days are discounted; student pays for 2 days
        expected_discount = Decimal('500.00')  # 100 per day * 5 days
        self.assertEqual(self.bill.discount, expected_discount)
        self.assertEqual(self.bill.calculate_total(), Decimal('2500.00'))  # 3000 - 500

    def test_discount_for_14_day_leave(self):
        """Test discount application for a 14-day continuous leave."""
        self.create_leave(14)
        self.bill.apply_leave_discount(timezone.now().month)
        
        # 10 days are discounted; student pays for 4 days
        expected_discount = Decimal('1000.00')  # 100 per day * 10 days
        self.assertEqual(self.bill.discount, expected_discount)
        self.assertEqual(self.bill.calculate_total(), Decimal('2000.00'))  # 3000 - 1000

    def test_no_discount_for_less_than_7_days(self):
        """Test that no discount is applied for leave less than 7 days."""
        self.create_leave(5)
        self.bill.apply_leave_discount(timezone.now().month)

        # No discount for fewer than 7 continuous days
        self.assertEqual(self.bill.discount, Decimal('0.00'))
        self.assertEqual(self.bill.calculate_total(), Decimal('3000.00'))

    def test_discount_for_21_day_leave(self):
        """Test discount application for a 21-day continuous leave."""
        self.create_leave(21)
        self.bill.apply_leave_discount(timezone.now().month)
        
        # 15 days are discounted; student pays for 6 days
        expected_discount = Decimal('1500.00')  # 100 per day * 15 days
        self.assertEqual(self.bill.discount, expected_discount)
        self.assertEqual(self.bill.calculate_total(), Decimal('1500.00'))  # 3000 - 1500

    def test_discount_for_28_day_leave(self):
        """Test discount application for a 28-day continuous leave."""
        self.create_leave(28)
        self.bill.apply_leave_discount(timezone.now().month)
        
        # 20 days are discounted; student pays for 8 days
        expected_discount = Decimal('2000.00')  # 100 per day * 20 days
        self.assertEqual(self.bill.discount, expected_discount)
        self.assertEqual(self.bill.calculate_total(), Decimal('1000.00'))  # 3000 - 2000

    def test_discount_for_leave_spanning_two_months(self):
        """Test discount application for a leave that spans two months."""
        current_date = timezone.now().date()
        # Create a leave that starts 10 days before the current month
        start_date = current_date.replace(day=1) - timedelta(days=10)
        end_date = current_date.replace(day=5)
        
        Leave.objects.create(student=self.student, start_date=start_date, end_date=end_date)
        
        self.bill.apply_leave_discount(current_date.month)
        
        # Assuming daily meal cost is 100, and only the days in the current month are considered
        # Total leave duration is 10 (from previous month) + 5 (current month) = 15
        # However, discount_days = 15 // 7 * 5 = 10
        expected_discount = Decimal('1000.00')  # 100 per day * 10 days
        self.assertEqual(self.bill.discount, expected_discount)
        self.assertEqual(self.bill.calculate_total(), Decimal('2000.00'))  # 3000 - 1000
