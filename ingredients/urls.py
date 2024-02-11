from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/ingredients/', consumers.IngredientsConsumer.as_asgi()),

]
