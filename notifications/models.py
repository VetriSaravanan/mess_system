# notifications/models.py

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username} - {self.message[:50]}"

    def mark_as_read(self):
        self.is_read = True
        self.save()

    @staticmethod
    def mark_all_as_read(user):
        """Mark all notifications for the user as read."""
        Notification.objects.filter(user=user, is_read=False).update(is_read=True)

    @staticmethod
    def get_unread_notifications(user):
        """Retrieve all unread notifications for the user."""
        return Notification.objects.filter(user=user, is_read=False)
