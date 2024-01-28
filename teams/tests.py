import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Team


class TeamModelTests(TestCase):
    def test_join_dateが未来の場合はis_joined_leagueはFalseを返す(self):
        future_join_team = Team(join_date=timezone.now() + datetime.timedelta(days=30))
        self.assertIs(future_join_team.is_joined_league(), False)
    
    def test_join_dateが過去かつleave_dateがnullの場合はTrueを返す(self):
        past_joined_team = Team(join_date=timezone.now() - timezone.timedelta(days=5))
        self.assertIs(past_joined_team.is_joined_league(), True)
    
    def test_join_dateが過去かつleave_dateが過去の場合はFalseを返す(self):
        already_left_team = Team(join_date=timezone.now() - timezone.timedelta(days=5)
                                 , leave_date=timezone.now() - timezone.timedelta(days=1))
        self.assertIs(already_left_team.is_joined_league(),False)
    
    def test_日付を指定してis_joined_leagueを呼び出せる(self):
        past_joined_team = Team(join_date=timezone.now() - timezone.timedelta(days=5))
        self.assertIs(past_joined_team.is_joined_league(date=timezone.now() - timezone.timedelta(days=1)),True)