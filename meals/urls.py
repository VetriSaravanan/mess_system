from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.meal_plan_overview, name='meals_index'),
    path('add_meal_plan/', views.add_meal_plan, name='add_meal_plan'),
    path('edit_meal_plan/<int:pk>/', views.edit_meal_plan, name='edit_meal_plan'),
    path('delete_meal_plan/<int:pk>/', views.delete_meal_plan, name='delete_meal_plan'),
]
