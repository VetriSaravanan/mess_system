from .models import Notification
from django.contrib.auth.models import User

def send_notification(user, message):
    """Utility function to send notifications to a specific user."""
    Notification.objects.create(user=user, message=message)
    notification.save()

def send_grocery_stock_alert(grocery):
    """Send a notification if grocery stock is low."""
    if grocery.stock_quantity < 10:  # Define your stock threshold here
        admins = User.objects.filter(is_staff=True)  # Send alert to admin users
        for admin in admins:
            send_notification(admin, f"Low stock alert: {grocery.name} is running low with {grocery.stock_quantity} items left.")
