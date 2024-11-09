import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_etsiminen(self):
        player = self.stats.search("Kurri")
        self.assertAlmostEqual(player.name, "Kurri")
        self.assertAlmostEqual(player.goals, 37)
    
    def test_etsiminen_ei_loydy(self):
        player = self.stats.search("EI OLE")
        self.assertEqual(player, None)

    def test_tiimin_pelaajat(self):
        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)
        self.assertTrue(all(player.team == "EDM" for player in players))
    
    def test_tiimin_pelaajat_ei_loydy(self):
        players = self.stats.team("ROSKA")
        self.assertEqual(players, [])
    
    def test_top_oikea_jarjestys_ja_maara(self):
        top_players = self.stats.top(3)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(len(top_players), 3)
    
    def test_top_yli_maaran(self):
        # Max 5
        top_players = self.stats.top(6)
        self.assertEqual(len(top_players), 5)