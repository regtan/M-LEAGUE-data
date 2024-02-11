from django.contrib import admin
from .models import DrawnRound, Round, HaiPai, WinningHand

admin.site.register(Round)
admin.site.register(HaiPai)
admin.site.register(WinningHand)
admin.site.register(DrawnRound)