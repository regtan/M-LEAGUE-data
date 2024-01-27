from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=255)
    name_kana = models.CharField(max_length=255)
    official_x_id = models.CharField(max_length=255)
    join_date = models.DateField("date joined league")