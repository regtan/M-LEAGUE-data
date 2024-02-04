from django.contrib import admin
from .models import Game, Round, GameBroadcaster

admin.site.register(Game)
admin.site.register(Round)
admin.site.register(GameBroadcaster)