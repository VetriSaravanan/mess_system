from django import forms
from .models import MealPlan, MealPlanGrocery
from django.forms.models import inlineformset_factory

# Form for MealPlan
class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ['date', 'meal_type', 'menu', 'cost']  # Fields for the meal plan

    # Adding custom styling or widgets if necessary (optional)
    def __init__(self, *args, **kwargs):
        super(MealPlanForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})  # Example of adding Bootstrap class to all fields

# Inline formset for associating groceries with a meal plan
MealPlanGroceryFormSet = inlineformset_factory(
    MealPlan,  # Parent model (MealPlan)
    MealPlanGrocery,  # Child model (MealPlanGrocery)
    fields=('grocery', 'quantity_used'),  # Fields in the formset
    extra=1,  # Number of empty grocery forms to display
    can_delete=True,  # Option to delete a grocery item
    widgets={
        'grocery': forms.Select(attrs={'class': 'form-control'}),
        'quantity_used': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
    }
)
