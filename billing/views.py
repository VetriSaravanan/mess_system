from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Bill
from .forms import PaymentForm
from students.models import Student  # Adjust as needed

@login_required
def bill_list(request):
    """View to list all unpaid bills for the student."""
    try:
        student = Student.objects.get(user=request.user)  # Get the Student instance linked to the user
        bills = Bill.objects.filter(student=student, is_paid=False)  # Filter unpaid bills for the student
    except Student.DoesNotExist:
        # Handle the case where the user is not linked to a Student instance
        bills = []
        # Optionally, add a message to inform the user
    bills = Bill.objects.all()
    return render(request, 'billing/bill_list.html', {'bills': bills})

@login_required
def pay_bill(request):
    """View to handle bill payments."""
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            bill = form.cleaned_data['bill']
            amount = form.cleaned_data['amount']
            if amount >= bill.calculate_total():  # Check if the payment is sufficient
                bill.is_paid = True
                bill.save()
                
                # Trigger notification to student and admin
                send_notification(bill.student.user, "Your bill has been paid successfully.")
                send_notification(request.user, "A bill has been paid.")
                
                return redirect('bill_list')
            else:
                form.add_error('amount', 'Insufficient amount to pay the bill.')
    else:
        form = PaymentForm()
    
    return render(request, 'billing/pay_bill.html', {'form': form})
