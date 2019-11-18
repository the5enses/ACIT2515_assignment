from unittest import TestCase
from league_player import LeaguePlayer

import inspect


class TestLeaguePlayers(TestCase):
    """unit test for class logPoint"""

    def setUp(self):
        """ Sets up test data and calls logPoint """
        self.logPoint()

        self.LeaguePlayer = LeaguePlayer(24, "Dendi", "Smith", "Bulldog", 23, 1, 2)
        self.assertIsNotNone(self.LeaguePlayer)

    def tearDown(self):
        """ Destroys test data and calls logPoint """
        self.logPoint()

    def logPoint(self):
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s -%s()' % (currentTest, callingFunction))

    def test_get_id(self):
        self.assertEqual(24, self.LeaguePlayer.get_id(), "id should be 24")

    def test_get_first_name(self):
        self.assertEqual("Dendi", self.LeaguePlayer.get_first_name(), "first name should should be Dendi")

    def test_get_last_name(self):
        self.assertEqual("Smith", self.LeaguePlayer.get_last_name(), "last name should should be Smith")

    def test_get_full_name(self):
        self.assertEqual("Dendi Smith", self.LeaguePlayer.get_full_name(), "first name should should be Dendi Smtih")

    def test_get_player_name(self):
        self.assertEqual("Bulldog", self.LeaguePlayer.get_player_name(), "player name should should be Bulldog")

    def test_get_age(self):
        self.assertEqual(23, self.LeaguePlayer.get_age(), "age should should be 23")

    def test_get_num_denies(self):
        self.assertEqual(1, self.LeaguePlayer.get_num_towers(), "number of towers should should be 1")

    def test_get_num_kills(self):
        self.assertEqual(2, self.LeaguePlayer.get_num_objectives(), "number of ojectives should should be 2")

    def test_get_details(self):
        self.assertEqual("Bulldog (Dendi Smith, age 23) has destroyed 1 towers and completed 2 objectives.",
                         self.LeaguePlayer.get_details(), "this should get details")

    def test_get_type(self):
        self.assertEqual("LeaguePlayer", self.LeaguePlayer.get_type(), "type should be LeaguePlayer")
