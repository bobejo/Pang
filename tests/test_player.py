import unittest
from src.Character import Character
from src.Player import Player, PlayerDeadException
from src.Cards import BeerCard, Suit


class TestPlayer(unittest.TestCase):

    def test_init(self):
        character = Character(name='Billie the Kid', health=5)
        player_samuel = Player(name='Samuel', role='Sheriff', character=character)
        self.assertEqual(player_samuel.health, 5)
        self.assertEqual(player_samuel.name, 'Samuel')
        self.assertEqual(player_samuel.role, 'Sheriff')
        self.assertIsNone(player_samuel.equipment)
        self.assertIsNone(player_samuel.weapon)
        self.assertEqual(len(player_samuel.hand), 0)

    def test_add_card(self):
        character = Character(name='Billie the Kid', health=5)
        player_samuel = Player(name='Samuel', role='Sheriff', character=character)
        self.assertEqual(len(player_samuel.hand), 0)
        player_samuel.add_cards(['Fake card1'])
        self.assertEqual(len(player_samuel.hand), 1)
        player_samuel.add_cards(['Fake card2'])
        self.assertEqual(len(player_samuel.hand), 2)

    def test_get_start_health(self):
        character = Character(name='Billie the Kid', health=5)
        player_samuel = Player(name='Samuel', role='Sheriff', character=character)
        self.assertEqual(player_samuel.get_start_health(), 5)

    def test_player_die(self):
        beer_card = BeerCard(Suit.HEARTS, 5)
        character = Character(name='Billie the Kid', health=1)
        player_samuel = Player(name='Samuel', role='Sheriff', character=character)
        self.assertEqual(player_samuel.health, 1)
        player_samuel.add_cards(beer_card)
        player_samuel.change_health(-1)
        self.assertEqual(player_samuel.health, 1)
        with self.assertRaises(PlayerDeadException):
            player_samuel.change_health(-1)
