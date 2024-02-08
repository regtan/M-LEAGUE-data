from django.contrib import admin
from .models import Game, Round, GameBroadcaster, GameResult, HaiPai, WinningHand

admin.site.register(Game)
admin.site.register(Round)
admin.site.register(GameBroadcaster)
admin.site.register(GameResult)
admin.site.register(HaiPai)
admin.site.register(WinningHand)