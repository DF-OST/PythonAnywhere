from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('ranking/', views.ranking, name='ranking'),
    path('<str:gender>/', views.form, name='form'),
    path('<str:gender>/result/', views.result, name='result'),

]