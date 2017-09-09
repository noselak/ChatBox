from django.shortcuts import render, redirect
from django.db import transaction
import haikunator
from .models import Room


hai = haikunator.Haikunator()

def about(request):
    """
    Starting page.
    """
    return render(request, 'chat/about.html')

def new_room(request):
    new_room = None
    while not new_room:
        with transaction.atomic():
            label = hai.haikunate()
            if Room.objects.filter(label=label).exists():
                continue
            new_room = Room.objects.create(label=label)
    return redirect('chat:chat_room', label=label)


def chat_room(request, label):
    room, created = Room.objects.get_or_create(label=label)
    messages = reversed(room.messages.order_by('-timestamp')[:50])
    template = 'chat/room.html'
    context = {
        'room': room,
        'messages': messages
    }

    return render(request, template, context)