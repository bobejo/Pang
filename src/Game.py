import random
import enum
import logging
import src.Cards as Cards
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
                player.add_cards(self.deck.take_top_card())

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
        :return:
        """
        player_index = self.players.index(self.active_player)

        possible_targets = []
        for i in range(player_index):
            possible_targets.append(self.players[i])
            possible_targets.append(self.players[i + player_index + 1])
        return set(possible_targets)

    def use_card(self, card, target=None):
        if isinstance(card, Cards.PangCard):
            if isinstance(target, Player):
                if target in self.get_possible_targets():
                    self.active_player.remove_card(card)
                    logging.info('Using pang! on {}'.format(target))
                    # TODO add miss card function
                    # TODO check barrel function
                    target.change_health(-1)
                else:
                    logging.info('Target {} is out of range.'.format(target))
            else:
                logging.info('Target {} is not a valid target for pang! card.'.format(target))
        elif isinstance(card, Cards.MissCard):
            if isinstance(target, Player):
                self.active_player.remove_card(card)
                # TODO create miss card trigger
                logging.info('Using miss card')
        elif isinstance(card, Cards.WellsFargoCard):
            logging.info('Using Wellsfargo, drawing 3 cards')
            self.active_player.remove_card(card)
            self.active_player.add_cards(self.deck.take_top_card(amount=3))
        elif isinstance(card, Cards.StageCoachCard):
            logging.info('Using StageCoach, drawing 2 cards')
            self.active_player.remove_card(card)
            self.active_player.add_cards(self.deck.take_top_card(amount=2))
        elif isinstance(card, Cards.HorseCard):
            logging.info('Riding Horse, setting evasion to 1')
            self.active_player.remove_card(card)
            self.active_player.evasion = 1
        elif isinstance(card, Cards.BarrelCard):
            logging.info('Equipping barrel, adding block')
            self.active_player.remove_card(card)
            self.active_player.remove_card(card)




class Roles(enum.Enum):
    """
    Enum representing each suit.
    """

    SHERIFF = 'Sheriff'
    OUTLAW = 'Outlaw'
    RENEGADE = 'Renegade'
    DEPUTY = 'Deputy'
