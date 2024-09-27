# attendance/forms.py
from django import forms
from .models import Leave

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ['start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
        
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date > end_date:
            raise forms.ValidationError("End date should be after start date.")
        return cleaned_data
