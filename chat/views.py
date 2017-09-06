from django.shortcuts import render
from .models import Room


def chat_room(request, label):
    room, created = Room.objects.get_or_create(label=label)
    messages = room.messages.order_by('-timestamp')[:50]
    template = 'chat/room.html'
    context = {
        'room': room,
        'messages': messages
    }

    return render(request, template, context)