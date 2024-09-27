from django import forms
from .models import Grocery

class GroceryForm(forms.ModelForm):
    class Meta:
        model = Grocery
        fields = ['name', 'stock_quantity', 'unit_price', 'daily_consumption']
