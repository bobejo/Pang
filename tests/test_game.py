import unittest
from src.Game import Game


class TestGame(unittest.TestCase):

    def test_init(self):
        pass

    def test_get_sheriff(self):
        pass

    def test_draw_start_hand(self):
        pass

    def test_create_players(self):
        pass

    def test_start_game(self):
        pass

    def test_use_card(self):
        pass

    def test_get_possible_targets(self):
        player_names = ['Samuel', 'Gustav', 'Maria', 'Andrea', 'Tomas', 'Mona', 'Lennart']
        game_object = Game(player_names)
        print(game_object.get_sheriff().name)
