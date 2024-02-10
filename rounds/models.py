from django.db import models
from games.models import Game
from members.models import Member

class Round(models.Model):
    WIND = [
        ('EAST','東'),
        ('SOUTH','南'),
    ]
    game = models.ForeignKey(Game,on_delete=models.CASCADE)
    round_wind = models.TextField('round wind',choices=WIND)
    round_number = models.IntegerField('round number')
    tsumibo = models.IntegerField('tsumibo')
    dead_wall = models.IntegerField('dead wall')

    def __str__(self):
        return str(self.game) + ":" + str(self.round_wind) + ":" + str(self.round_number) + "局" + ":" + str(self.tsumibo) + '本場'

class HaiPai(models.Model):
    SEATS = [
        ('EAST','東'),
        ('SOUTH','南'),
        ('WEST','西'),
        ('NORTH','北'),
    ]
    round = models.ForeignKey(Round,on_delete=models.CASCADE)
    seats = models.CharField('seats',max_length=255,choices=SEATS)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    hai_pai = models.CharField('hai pai',max_length=255,null=True,blank=True)
    syanten = models.IntegerField('syanten',editable=False,null=True,blank=True)

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
    fuu = models.IntegerField('fuu')
    faan = models.IntegerField('faan')
    winning_score = models.IntegerField('winning score',editable=False)