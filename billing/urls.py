from django.urls import path
from . import views

urlpatterns = [
    path('bill/', views.bill_list, name='bill_list'),
    path('bills/', views.bill_list, name='bill_list'),  # Add this line
    path('pay/', views.pay_bill, name='pay_bill'),
]
