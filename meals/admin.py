# meals/admin.py
from django.contrib import admin
from .models import MealPlan, Grocery

@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('date', 'cost_per_day')
    list_filter = ('date',)
    search_fields = ('date', 'menu')

@admin.register(Grocery)
class GroceryAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock_quantity', 'unit_price', 'consumption_per_day')
    list_filter = ('name',)
    search_fields = ('name',)
