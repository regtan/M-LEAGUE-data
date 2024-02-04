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