from django.test import TestCase
from .models import Grocery
from decimal import Decimal

class GroceryModelTest(TestCase):
    def setUp(self):
        self.grocery = Grocery.objects.create(name='Sugar', stock_quantity=50, unit_price=Decimal('40.00'), daily_consumption=Decimal('2.00'))

    def test_grocery_cost_calculation(self):
        """Test that the grocery cost is calculated correctly."""
        self.assertEqual(self.grocery.calculate_cost(), Decimal('80.00'))

    def test_grocery_update_stock(self):
        """Test that the grocery stock is updated after consumption."""
        self.grocery.update_stock_consumption(2)  # Update this method call
        self.assertEqual(self.grocery.stock_quantity, 48)
