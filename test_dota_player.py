from unittest import TestCase
from dota_player import DotaPlayer

import inspect


class TestDotaPlayer(TestCase):
    """unit test for class logPoint"""

    def setUp(self):
        """ Sets up test data and calls logPoint """
        self.logPoint()

        self.DotaPlayer = DotaPlayer(24, "Dendi", "Smith", "Bulldog", 23, 1, 2, 3)
        self.assertIsNotNone(self.DotaPlayer)

    def tearDown(self):
        """ Destroys test data and calls logPoint """
        self.logPoint()

    def logPoint(self):
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s -%s()' % (currentTest, callingFunction))

    def test_get_id(self):
        self.assertEqual(24, self.DotaPlayer.get_id(), "id should be 24")

    def test_get_first_name(self):
        self.assertEqual("Dendi", self.DotaPlayer.get_first_name(), "first name should should be Dendi")

    def test_get_last_name(self):
        self.assertEqual("Smith", self.DotaPlayer.get_last_name(), "last name should should be Smith")

    def test_get_full_name(self):
        self.assertEqual("Dendi Smith", self.DotaPlayer.get_full_name(), "first name should should be Dendi Smtih")

    def test_get_player_name(self):
        self.assertEqual("Bulldog", self.DotaPlayer.get_player_name(), "player name should should be Bulldog")

    def test_get_age(self):
        self.assertEqual(23, self.DotaPlayer.get_age(), "age should should be 23")

    def test_get_num_denies(self):
        self.assertEqual(1, self.DotaPlayer.get_num_denies(), "number of denies should should be 1")

    def test_get_num_kills(self):
        self.assertEqual(2, self.DotaPlayer.get_num_kills(), "number of kills should should be 2")

    def test_num_deaths(self):
        self.assertEqual(3, self.DotaPlayer.get_num_deaths(), "number of deaths should should be 3")

    def test_get_details(self):
        self.assertEqual("Bulldog (Dendi Smith, age 23) has 1 denies, 2 kills, and 3 deaths.",
                         self.DotaPlayer.get_details(), "this should get details")

    def test_get_type(self):
        self.assertEqual("DotaPlayer", self.DotaPlayer.get_type(), "type should be DotaPlayer")

