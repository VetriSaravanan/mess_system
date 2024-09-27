from django.urls import path
from . import views

urlpatterns = [
    path('grocery-list/', views.grocery_list, name='grocery_list'),
    path('grocery/add/', views.add_grocery, name='add_grocery'),
    path('grocery/update/<int:pk>/', views.update_grocery, name='update_grocery'),
    path('grocery/delete/<int:pk>/', views.delete_grocery, name='delete_grocery'),
]
