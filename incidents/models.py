from django.db import models
from rounds.models import Round
from members.models import Member

class Incident(models.Model):
    RULING_TYPES = [
        ('NONE', 'なし'),
        ('NO_WINNING','あがり放棄'),
        ('CHOOMBON', 'チョンボ'),
        ('REDCARD', 'レッドカード'),
        ('YELLOWCARD', 'イエローカード'),
    ]
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    ruling = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.description