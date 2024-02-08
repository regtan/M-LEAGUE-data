from collections.abc import Iterable
from django.db import models
from game_days.models import GameDay
from members.models import Member

class Game(models.Model):
    game_day = models.ForeignKey(GameDay,on_delete=models.CASCADE)
    game_number = models.IntegerField("game number")
    start_east = models.ForeignKey(Member,on_delete=models.CASCADE,related_name='start_east')
    start_south = models.ForeignKey(Member,on_delete=models.CASCADE,related_name='start_south')
    start_west = models.ForeignKey(Member,on_delete=models.CASCADE,related_name='start_west')
    start_north = models.ForeignKey(Member,on_delete=models.CASCADE,related_name='start_north')

    def __str__(self):
        return str(self.game_day) + ":" + str(self.game_number)

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

class GameBroadcaster(models.Model):
    BROADCASTER_TYPE = [
        ('CASTER','実況'),
        ('COMMENTATOR','解説'),
        ('PLAYER_COMMENTATOR','プレイヤー解説'),
        ('INTERVIEWER','インタビュー'),
    ]
    game = models.ForeignKey(Game,on_delete=models.CASCADE)
    broadcaster_type = models.TextField('broadcaster type',choices=BROADCASTER_TYPE)
    broadcaster = models.ForeignKey('broadcasters.Broadcaster',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.game) + ":" + str(self.broadcaster)

class GameResult(models.Model):
    POSITION = [
        (1,'1位'),
        (2,'2位'),
        (3,'3位'),
        (4,'4位'),
        (1.5,'同点1位'),
        (2.5,'同点2位'),
        (3.5,'同点3位'),
        (4.5,'同点4位'),
    ]

    BASE_SCORE = 30000
    
    game = models.ForeignKey(Game,on_delete=models.CASCADE)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    position = models.FloatField('position',choices=POSITION)
    row_score = models.IntegerField('row score')
    position_score = models.IntegerField('position score')
    total_score = models.FloatField('total score',editable=False)

    def calc_total_score(self,row_score,position_score,base_score):
        return (row_score + position_score - base_score)/1000

    def save(self,*args,**kwargs):
        self.total_score = self.calc_total_score(self.row_score,self.position_score,self.BASE_SCORE)
        super().save(*args,**kwargs)

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