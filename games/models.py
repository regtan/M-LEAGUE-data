from django.db import models
from game_days.models import GameDay
from members.models import Member

class Game(models.Model):
    game_day = models.ForeignKey(GameDay,on_delete=models.CASCADE)
    game_number = models.IntegerField("game number")
    start_east = models.ForeignKey(Member,on_delete=models.CASCADE,related_name="start at east")
    start_south = models.ForeignKey(Member,on_delete=models.CASCADE,related_name="start at south")
    start_west = models.ForeignKey(Member,on_delete=models.CASCADE,related_name="start at west")
    start_north = models.ForeignKey(Member,on_delete=models.CASCADE,related_name="start at north")

    def __str__(self):
        return self.game_day + ":" + self.game_number

