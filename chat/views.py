from django.shortcuts import render, redirect
import haikunator
from .models import Room


def about(request):
    """
    Starting page.
    """
    return render(request, 'chat/about.html')

def new_room(request):
    new_room = None
    while new_room is None:
        label = haikunator.haikunate()
        if Room.objects.filter(label=label).exists():
            continue
        new_room = Room.objects.create(label=label)
    return redirect('chat:chat_room', label=label)


def chat_room(request, label):
    room, created = Room.objects.get_or_create(label=label)
    messages = room.messages.order_by('-timestamp')[:50]
    template = 'chat/room.html'
    context = {
        'room': room,
        'messages': messages
    }

    return render(request, template, context)