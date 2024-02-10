from django.contrib import admin
from .models import Game, GameBroadcaster, GameResult

admin.site.register(Game)
admin.site.register(GameBroadcaster)
admin.site.register(GameResult)
