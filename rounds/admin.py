from django.contrib import admin
from .models import DrawnRound, Round, HaiPai, Fuuro, RoundResult

admin.site.register(Round)
admin.site.register(HaiPai)
admin.site.register(DrawnRound)
admin.site.register(Fuuro)
admin.site.register(RoundResult)