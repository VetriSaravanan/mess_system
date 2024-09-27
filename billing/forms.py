from django import forms
from .models import Bill

class PaymentForm(forms.Form):
    bill = forms.ModelChoiceField(queryset=Bill.objects.filter(is_paid=False), label='Select Bill')
    amount = forms.DecimalField(max_digits=7, decimal_places=2, label='Amount to Pay')
