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

    def test_haku(self):
        pelaaja = self.stats.search("Semenko")
        self.assertAlmostEqual(pelaaja.name, "Semenko")

    def test_haettua_pelaajaa_ei_ole(self):
        pelaaja = self.stats.search("Moilanen")
        self.assertIsNone(pelaaja)

    def test_team_antaa_joukkueen_pelaajat(self):
        tiimin_pelaajat = self.stats.team("EDM")
        tiimin_pelaajat = {pelaaja.name for pelaaja in tiimin_pelaajat}
        oletetut_pelaajat = {"Semenko", "Kurri", "Gretzky"}
        self.assertAlmostEqual(tiimin_pelaajat, oletetut_pelaajat)

    def test_top_antaa_parhaat_pelaajat(self):
        top_pelaajat = self.stats.top(3)
        self.assertEqual(top_pelaajat[0].name, "Gretzky")
        self.assertEqual(top_pelaajat[1].name, "Lemieux")
        self.assertEqual(top_pelaajat[2].name, "Yzerman")