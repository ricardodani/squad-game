from django.contrib import admin
from .models import (
    Game, GameCategory, GamePlayer, GameRound, PlayerFact, PlayerRoundScore
)

admin.site.register(Game)
admin.site.register(GameCategory)
admin.site.register(GamePlayer)
admin.site.register(GameRound)
admin.site.register(PlayerFact)
admin.site.register(PlayerRoundScore)