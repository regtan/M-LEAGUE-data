from django.db import models
from rounds.models import Round
from members.models import Member

class WinningHand(models.Model):
    WINNING_TYPE = [
        ('TSUMO','ツモ'),
        ('RON','ロン'),
    ]
    round = models.ForeignKey(Round,on_delete=models.CASCADE)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    winning_type = models.CharField('tsumo ron',max_length=255,choices=WINNING_TYPE)
    is_dealer = models.BooleanField('is dealer')
    winning_hands = models.CharField('winning hands',max_length=255)
    winning_pai = models.CharField('winning hands',max_length=255)
    fuu = models.IntegerField('fuu')
    faan = models.IntegerField('faan')
    winning_score = models.IntegerField('winning score',editable=False)
    additional_score = models.IntegerField('additional score',editable=False)
