import datetime
from django.db import models
from django.utils import timezone

class Team(models.Model):
    name = models.CharField(max_length=255)
    name_kana = models.CharField(max_length=255)
    official_x_id = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    join_date = models.DateField("date joined league")
    leave_date = models.DateField("date left league",null=True,blank=True)

    def __str__(self):
        return self.name
    
    def is_joined_league(self,date=timezone.now()):
        return self.join_date <= date and (self.leave_date is None or self.leave_date > date)