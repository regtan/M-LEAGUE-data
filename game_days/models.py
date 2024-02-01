from django.db import models
from seasons.models import Season

class GameDay(models.Model):
    MATCH_TYPE = [
        ('LEGULAR','legular'),
        ('SEMI_FINAL','semi final'),
        ('FINAL','final')
    ]

    season = models.ForeignKey('seasons.Season',on_delete=models.CASCADE)
    match_type = models.TextField('match type',choices=MATCH_TYPE)
    total_game_days = models.IntegerField("total game days")
    game_date = models.DateField("date on game")
    archive_url = models.URLField("archive url")
    