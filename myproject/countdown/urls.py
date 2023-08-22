from django.urls import path
from . import views
from .views import *

app_name = 'events'

urlpatterns = [
    path('', views.list, name='list'),
    path('<pk>/', EventDetailView.as_view(), name='event-detail'),
]