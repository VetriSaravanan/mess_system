from django.shortcuts import render, redirect, get_object_or_404
from .forms import MealPlanForm, MealPlanGroceryFormSet  # Ensure formset is imported
from .models import MealPlan


# View for adding a new meal plan
def add_meal_plan(request):
    if request.method == 'POST':
        form = MealPlanForm(request.POST)
        formset = MealPlanGroceryFormSet(request.POST)  # Formset for groceries
        if form.is_valid() and formset.is_valid():
            meal_plan = form.save()  # Save meal plan
            for form in formset:
                meal_plan_grocery = form.save(commit=False)
                meal_plan_grocery.meal_plan = meal_plan  # Link grocery to meal plan
                meal_plan_grocery.save()
            return redirect('meals/meals_index')  # Redirect to overview
    else:
        form = MealPlanForm()
        formset = MealPlanGroceryFormSet()  # Empty formset
    return render(request, 'meals/add_meal_plan.html', {'form': form, 'formset': formset})


# View for editing an existing meal plan
def edit_meal_plan(request, pk):
    meal_plan = get_object_or_404(MealPlan, pk=pk)
    if request.method == 'POST':
        form = MealPlanForm(request.POST, instance=meal_plan)
        formset = MealPlanGroceryFormSet(request.POST, instance=meal_plan)
        if form.is_valid() and formset.is_valid():
            form.save()  # Save meal plan
            formset.save()  # Save associated groceries
            return redirect('meals/meals_index')
    else:
        form = MealPlanForm(instance=meal_plan)
        formset = MealPlanGroceryFormSet(instance=meal_plan)
    return render(request, 'meals/edit_meal_plan.html', {'form': form, 'formset': formset})


# View for deleting a meal plan
def delete_meal_plan(request, pk):
    meal_plan = get_object_or_404(MealPlan, pk=pk)
    if request.method == 'POST':
        meal_plan.delete()
        return redirect('meals/meal_plan_overview')
    return render(request, 'meals/delete_meal_plan.html', {'meal_plan': meal_plan})


# Meal Plan Overview: Show all meal plans
def meal_plan_overview(request):
    meal_plans = MealPlan.objects.all()  # Fetch all meal plans
    return render(request, 'meals/meal_plan_overview.html', {'meal_plans': meal_plans})
