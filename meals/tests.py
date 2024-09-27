from django.test import TestCase
from .models import MealPlan, MealPlanGrocery
from grocery.models import Grocery
from decimal import Decimal
from datetime import date

class MealPlanModelTest(TestCase):
    def setUp(self):
        # Create mock grocery items
        self.grocery1 = Grocery.objects.create(name='Rice', stock_quantity=100, unit_price=Decimal('20.00'))
        self.grocery2 = Grocery.objects.create(name='Lentils', stock_quantity=50, unit_price=Decimal('15.00'))
        
        # Create a meal plan
        self.meal_plan = MealPlan.objects.create(date=date.today(), meal_type='lunch', menu="Rice, Lentils", cost=Decimal('100.00'))
        
        # Associate groceries with the meal plan, including cost_for_grocery
        MealPlanGrocery.objects.create(
            meal_plan=self.meal_plan,
            grocery=self.grocery1,
            quantity_used=Decimal('5.00'),
            cost_for_grocery=Decimal('100.00')  # Assuming cost is directly related to quantity
        )
        MealPlanGrocery.objects.create(
            meal_plan=self.meal_plan,
            grocery=self.grocery2,
            quantity_used=Decimal('3.00'),
            cost_for_grocery=Decimal('45.00')  # Assuming cost is directly related to quantity
        )

    def test_meal_plan_grocery_association(self):
        """Test that groceries are correctly associated with the meal plan."""
        self.assertEqual(self.meal_plan.groceries.count(), 2)
    
    def test_serve_meal_updates_stock(self):
        """Test that serving a meal updates the grocery stock correctly."""
        self.meal_plan.serve_meal()
        self.grocery1.refresh_from_db()
        self.grocery2.refresh_from_db()
        self.assertEqual(self.grocery1.stock_quantity, 95)
        self.assertEqual(self.grocery2.stock_quantity, 47)
