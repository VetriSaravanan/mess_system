from django.contrib.auth.models import AbstractUser
from django.db import models
from decimal import Decimal 

class CustomUser(AbstractUser):
    STUDENT = 'student'
    ADMIN = 'admin'
    MESS_STAFF = 'mess_staff'

    ROLE_CHOICES = [
        (STUDENT, 'Student'),
        (ADMIN, 'Admin'),
        (MESS_STAFF, 'Mess Staff'),
    ]

    # Ensure role choices are set properly
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"

    # Role-checking helper methods
    def is_student(self):
        return self.role == self.STUDENT

    def is_admin(self):
        return self.role == self.ADMIN

    def is_mess_staff(self):
        return self.role == self.MESS_STAFF


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
    registration_number = models.CharField(max_length=20, unique=True)
    hostel_status = models.BooleanField(default=True)  # True if staying in the hostel
    daily_meal_cost = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return f"{self.user.username} - {self.registration_number}"
