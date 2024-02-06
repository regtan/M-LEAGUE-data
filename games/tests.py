from django.test import TestCase
from .models import GameResult

class GameResultTestCase(TestCase):
    def test_素点36400点順位点50000点(self):
        game_result = GameResult(row_score=36400, position_score=50000)
        self.assertEqual(game_result.calc_total_score(game_result.row_score,game_result.position_score,game_result.BASE_SCORE), 56.4)
    
    def test_素点18000点順位点マイナス30000点(self):
        game_result = GameResult(row_score=18000, position_score=-30000)
        self.assertEqual(game_result.calc_total_score(game_result.row_score,game_result.position_score,game_result.BASE_SCORE), -42.0)