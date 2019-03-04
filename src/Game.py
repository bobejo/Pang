import random
import enum
from src.Deck import StandardDeck
from src.Player import Player
from src.Character import Character

class Game:
    def __init__(self, player_names):
        self.player_names = player_names
        self.deck = StandardDeck()
        self.players = self.create_players()
        self.sheriff = self.get_sheriff()
        self.active_player = self.sheriff

    def start_game(self):
        pass

    def use_card(self, card):
        pass

    def create_players(self):
        roles = [Roles.SHERIFF, Roles.OUTLAW, Roles.RENEGADE, Roles.DEPUTY, Roles.OUTLAW, Roles.OUTLAW, Roles.DEPUTY]
        amount_of_players = len(self.player_names)
        players = []
        if amount_of_players <= len(roles):
            roles = roles[:amount_of_players]
            random.shuffle(roles)

            for player, role in zip(self.player_names, roles):
                players.append(Player(name=player, role=role, character=self.get_character()))
            return players
        else:
            raise IndexError('Invalid amount of players')

    def draw_start_hand(self):
        for player in self.players:
            for i in range(player.health):
                player.add_card(self.deck.take_top_card())

    def get_sheriff(self):
        for player in self.players:
            if player.role == Roles.SHERIFF:
                return player

    def get_character(self):
        """
        Return the character chosen by the player
        :return:
        """
        # TODO fix function
        return Character(name='Billie the Kid', health=5)

    def get_possible_targets(self):
        """
        Returns all players the player can target with limited range cards
        :param player:
        :return:
        """
        player_index = self.players.index(self.active_player)

        possible_targets = []
        for i in range(player_index):
            possible_targets.append(self.players[i])
            possible_targets.append(self.players[i + player_index + 1])
        return set(possible_targets)


class Roles(enum.Enum):
    """
    Enum representing each suit.
    """

    SHERIFF = 'Sheriff'
    OUTLAW = 'Outlaw'
    RENEGADE = 'Renegade'
    DEPUTY = 'Deputy'
