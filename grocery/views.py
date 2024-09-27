from django.shortcuts import render, redirect, get_object_or_404
from .models import Grocery
from .forms import GroceryForm
from notifications.utils import send_grocery_stock_alert  # Import utility for notifications

def grocery_list(request):
    groceries = Grocery.objects.all()
    return render(request, 'grocery/grocery_list.html', {'groceries': groceries})

def add_grocery(request):
    if request.method == 'POST':
        form = GroceryForm(request.POST)
        if form.is_valid():
            grocery = form.save()
            send_grocery_stock_alert(grocery)  # Trigger notification after adding new grocery
            return redirect('grocery_list')
    else:
        form = GroceryForm()
    return render(request, 'grocery/add_grocery.html', {'form': form})

def update_grocery(request, pk):
    grocery = get_object_or_404(Grocery, pk=pk)
    if request.method == 'POST':
        form = GroceryForm(request.POST, instance=grocery)
        if form.is_valid():
            grocery = form.save()
            send_grocery_stock_alert(grocery)  # Trigger notification if stock is low
            return redirect('grocery_list')
    else:
        form = GroceryForm(instance=grocery)
    return render(request, 'grocery/update_grocery.html', {'form': form})

def delete_grocery(request, pk):
    grocery = get_object_or_404(Grocery, pk=pk)
    if request.method == 'POST':
        grocery.delete()
        return redirect('grocery_list')
    return render(request, 'grocery/delete_grocery.html', {'grocery': grocery})
