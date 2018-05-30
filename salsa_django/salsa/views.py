from django.shortcuts import render

from .models import Event

def event_list(request):
    events = Event.objects.all()
    return render(request, 'salsa/event_list.html', {'events': events})

def event_detail(request, pk):
    event = Event.objects.get(id=pk)
    return render(request, 'salsa/event_detail.html', {'event': event})