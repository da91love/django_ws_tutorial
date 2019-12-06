# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
from .consumers import ChatConsumer

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
from django.views.decorators.csrf import csrf_exempt
from events import Events

events = Events()

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

@csrf_exempt
def listener(request):
    try:
        status = request.GET.get('status', None)
        progress = request.GET.get('progress', None)
        message = request.GET.get('message', None)

        layer = get_channel_layer()
        async_to_sync(layer.group_send)('event', {
            'type': 'listener',
            'content': {
                'status': status,
                'progress': progress,
                'message': message,
            }
        })

    except Exception as e:
        raise e