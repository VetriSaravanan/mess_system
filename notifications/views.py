from django.shortcuts import render, redirect, get_object_or_404
from .models import Notification

def notification_list(request):
    """View to list all notifications for the logged-in user."""
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    return render(request, 'notifications/notification_list.html', {'notifications': notifications})

def mark_as_read(request, notification_id):
    """View to mark a notification as read."""
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.mark_as_read()
    return redirect('notification_list')
