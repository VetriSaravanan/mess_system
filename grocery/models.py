from django.db import models

class Grocery(models.Model):
    name = models.CharField(max_length=100)
    stock_quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    daily_consumption = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.name} - {self.stock_quantity} units"

    def calculate_cost(self):
        """Calculate total cost based on unit price and daily consumption."""
        return self.daily_consumption * self.unit_price

    def update_stock_consumption(self, quantity):
        """Update stock based on the quantity consumed."""
        if self.stock_quantity >= quantity:
            self.stock_quantity -= quantity
            self.save()
        else:
            raise ValueError(f"Not enough stock for {self.name}. Available: {self.stock_quantity}, Required: {quantity}")

    @property
    def consumption_per_day(self):
        """Property to return daily consumption."""
        return self.daily_consumption
