import unittest
from src.Game import Game, InvalidTargetException, StartGameException
import src.Cards as Cards


class TestGame(unittest.TestCase):

    def test_init(self):
        pass

    def test_get_sheriff(self):
        pass

    def test_draw_start_hand(self):
        player_names = ['Samuel', 'Gustav', 'Maria', 'Andrea', 'Tomas', 'Mona', 'Lennart']
        game_object = Game(player_names)
        game_object.draw_start_hand()
        for player in game_object.players:
            self.assertEqual(player.health, len(player.hand))

    def test_create_players(self):
        player_names = ['Samuel', 'Gustav', 'Maria', 'Andrea', 'Tomas', 'Mona', 'Lennart']
        game_object = Game(player_names)
        self.assertEqual(len(game_object.players), len(player_names))

    def test_create_players_exception(self):
        player_names = ['Samuel', 'Gustav', 'Maria', 'Andrea', 'Tomas', 'Mona', 'Lennart', 'Monna']
        with self.assertRaises(StartGameException):
            game_object = Game(player_names)


    def test_start_game(self):
        pass

    def test_get_possible_targets(self):
        pistol = Cards.PistolCard(Cards.Suit.DIAMONDS, 5)
        player_names = ['Samuel', 'Gustav', 'Maria', 'Andrea', 'Tomas', 'Mona', 'Lennart']
        game_object = Game(player_names)
        game_object.active_player = game_object.players[3]
        found_targets = game_object.get_possible_targets()
        self.assertEqual(found_targets, [game_object.players[2], game_object.players[4]])

        game_object.active_player = game_object.players[5]
        game_object.active_player.add_cards([pistol])
        game_object.use_card(pistol)
        found_targets = game_object.get_possible_targets()

        self.assertEqual(found_targets, [game_object.players[3], game_object.players[4],
                                         game_object.players[6], game_object.players[0]])

    def test_use_bang_cards(self):
        bang_card1 = Cards.PangCard(Cards.Suit.SPADES, 2)
        bang_card2 = Cards.PangCard(Cards.Suit.HEARTS, 8)
        player_names = ['Samuel', 'Gustav', 'Maria', 'Andrea', 'Tomas', 'Mona', 'Lennart']
        game_object = Game(player_names)
        game_object.active_player = game_object.players[3]

        game_object.active_player.add_cards([bang_card1, bang_card2])
        self.assertEqual(game_object.players[4].health, 5)
        self.assertEqual(len(game_object.active_player.hand), 2)
        game_object.use_card(bang_card1, game_object.players[4])
        self.assertEqual(len(game_object.active_player.hand), 1)
        self.assertEqual(game_object.players[4].health, 4)
        with self.assertRaises(InvalidTargetException):
            game_object.use_card(bang_card2, game_object.players[6])
        self.assertEqual(len(game_object.active_player.hand), 1)

    def test_use_miss_cards(self):
        pass

    def test_use_equipment_cards(self):
        scope = Cards.ScopeCard(Cards.Suit.CLUBS, 6)
        barrel = Cards.BarrelCard(Cards.Suit.DIAMONDS, 7)
        horse = Cards.HorseCard(Cards.Suit.HEARTS, 8)
        player_names = ['Samuel', 'Gustav', 'Maria', 'Andrea', 'Tomas', 'Mona', 'Lennart']
        game_object = Game(player_names)
        game_object.active_player.add_cards([scope, barrel, horse])
        self.assertIsNone(game_object.active_player.equipment)
        game_object.use_card(horse)
        self.assertEqual(game_object.active_player.equipment, horse)
        game_object.use_card(barrel)
        self.assertEqual(game_object.active_player.equipment, barrel)
        game_object.use_card(scope)
        self.assertEqual(game_object.active_player.equipment, scope)

    def test_use_weapon_cards(self):
        rifle = Cards.RifleCard(Cards.Suit.CLUBS, 5)
        pistol = Cards.PistolCard(Cards.Suit.HEARTS, 8)
        player_names = ['Samuel', 'Gustav', 'Maria', 'Andrea', 'Tomas', 'Mona', 'Lennart']
        game_object = Game(player_names)
        game_object.active_player.add_cards([pistol, rifle])
        self.assertIsNone(game_object.active_player.weapon)
        game_object.use_card(rifle)
        self.assertEqual(game_object.active_player.weapon, rifle)
        game_object.use_card(pistol)
        self.assertEqual(game_object.active_player.weapon, pistol)

    def test_use_draw_cards(self):

        draw_card1 = Cards.WellsFargoCard(Cards.Suit.CLUBS, 5)
        draw_card2 = Cards.StageCoachCard(Cards.Suit.HEARTS, 8)
        player_names = ['Samuel', 'Gustav', 'Maria', 'Andrea', 'Tomas', 'Mona', 'Lennart']
        game_object = Game(player_names)

        game_object.active_player.add_cards([draw_card1, draw_card2])
        self.assertEqual(len(game_object.active_player.hand), 2)
        game_object.use_card(draw_card1)
        self.assertEqual(len(game_object.active_player.hand), 4)
        game_object.use_card(draw_card2)
        self.assertEqual(len(game_object.active_player.hand), 5)
