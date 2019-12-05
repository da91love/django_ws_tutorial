from django.urls import re_path

from . import consumers
from . import consumers_channel

websocket_urlpatterns = [
    # re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers_channel.ChatConsumer),
]