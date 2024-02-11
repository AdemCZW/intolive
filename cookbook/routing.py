from django.urls import path
from ingredients.consumers import IngredientsConsumer

websocket_urlpatterns = [
    path('ws/ingredients/', IngredientsConsumer.as_asgi()),
    # 添加其他 WebSocket 路由
]
