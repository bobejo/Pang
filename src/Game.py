import random
import enum
from src.Deck import StandardDeck
from src.Player import Player


class Game:
    def __init__(self, player_names):
        self.player_names = player_names
        self.deck = StandardDeck()
        self.players = []
        self.active_player = None
        self.sheriff = self.get_sheriff()

    def start_game(self):
        self.deck = StandardDeck.create_deck()

    def use_card(self, card):
        pass

    def create_players(self):
        roles = [Roles.SHERIFF, Roles.OUTLAW, Roles.RENEGADE, Roles.DEPUTY, Roles.OUTLAW, Roles.OUTLAW, Roles.DEPUTY]
        amount_of_players = len(self.player_names)

        if amount_of_players <= len(roles):
            roles = roles[:amount_of_players]
            random.shuffle(roles)

            for player, role in zip(self.player_names, roles):
                self.players.append(Player(name=player, role=role, character=self.get_character()))

        else:
            raise IndexError('Invalid amount of players')

    def draw_start_hand(self):
        for player in self.players:
            for i in range(player.health):
                player.add_card(self.deck.take_top_card())

    def get_sheriff(self):
        for player in self.players:
            if player.role == Player.role == Roles.SHERIFF:
                return player

    def get_character(self):
        return None


class Roles(enum.Enum):
    """
    Enum representing each suit.
    """

    SHERIFF = 'Sheriff'
    OUTLAW = 'Outlaw'
    RENEGADE = 'Renegade'
    DEPUTY = 'Deputy'
