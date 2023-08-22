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

def list(request):
    events = Event.objects.order_by('when')
    return render(request, 'countdown/main.html', {'object_list': events})