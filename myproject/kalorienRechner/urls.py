from django.urls import path
from . import views

urlpatterns = [
    path('', views.meal_list_today, name='meal_list_today'),
    path('history/', views.meal_history_list, name='meal_history_list'),
    path('history/<str:date>', views.meal_history_list, name='meal_history_list'),
    path('meal/<int:pk>/', views.meal_detail, name='meal_detail'),
    path('meal/new/', views.meal_new, name='meal_new'),
    path('meal/edit/<int:pk>/', views.meal_edit, name='meal_edit'),
]