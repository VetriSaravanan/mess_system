from django.db import models
from grocery.models import Grocery

class MealPlan(models.Model):
    MEAL_TYPES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    ]

    date = models.DateField()
    meal_type = models.CharField(max_length=10, choices=MEAL_TYPES)
    menu = models.TextField()  # Stores the menu details
    cost = models.DecimalField(max_digits=7, decimal_places=2)  # Stores the cost for each meal
    groceries = models.ManyToManyField(Grocery, through='MealPlanGrocery')  # Track groceries used in the meal

    def __str__(self):
        return f"{self.date} - {self.meal_type}"

    def serve_meal(self):
        """Update grocery stock based on meal consumption."""
        for meal_plan_grocery in self.mealplangrocery_set.all():
            meal_plan_grocery.grocery.update_stock_consumption(meal_plan_grocery.quantity_used)

    @property
    def cost_per_day(self):
        """Calculate the total cost for the day based on groceries used."""
        total_cost = 0
        for meal_plan_grocery in self.mealplangrocery_set.all():
            total_cost += meal_plan_grocery.cost_for_grocery
        return total_cost


class MealPlanGrocery(models.Model):
    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE)
    grocery = models.ForeignKey(Grocery, on_delete=models.CASCADE)
    quantity_used = models.DecimalField(max_digits=6, decimal_places=2)
    cost_for_grocery = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Add this to store the cost per grocery used

    def __str__(self):
        return f"{self.meal_plan} - {self.grocery} ({self.quantity_used} units)"
