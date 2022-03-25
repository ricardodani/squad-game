from django.urls import path
from .views import create_game, join_game, detail_game, create_category

urlpatterns = [
    path('create', create_game, name="create-game"),
    path('join', join_game, name="join-game"),
    path('game/<code>', detail_game, name="join-game"),
    path('game/<code>/category', create_category, name="create-category"),
]
