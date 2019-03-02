import random
from src.Deck import StandardDeck
from src.Player import Player

class Game():
    def __init__(self, player_names):
        self.player_names = player_names
        self.deck = None
        self.active_player = None
        self.players = []


    def start_game(self):
        self.deck = StandardDeck.create_deck()



    def use_card(self, card):
        pass

    def create_players(self):
        roles = ['Sheriff', 'Outlaw', 'Renegade', 'Deputy', 'Outlaw', 'Outlaw', 'Deputy']
        amount_of_players = len(self.player_names)

        if amount_of_players <= len(roles):
            roles = roles[:amount_of_players]
            random.shuffle(roles)

            for p, r in zip(self.player_names, roles):
                self.players.append(Player(name=p, roles=r, character=None))

        else:
            raise IndexError('Invalid amount of players')




