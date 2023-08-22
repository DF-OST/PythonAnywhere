from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Event

# Create your views here.
class EventListView(ListView):
    model = Event
    template_name = 'countdown/main.html'


class EventDetailView(DetailView):
    model = Event
    template_name = 'countdown/countdown.html'