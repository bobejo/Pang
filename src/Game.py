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
        player_range = 1
        if self.active_player.weapon:
            player_range = self.active_player.weapon.weapon_range
        if isinstance(self.active_player.equipment, Cards.ScopeCard):
            player_range += 1
        if player_range >= 3:
            return self.players.remove(self.active_player)
        possible_targets = []
        players = self.players.copy()
        players.extend(players)

        for i in range(player_index-player_range, player_index+player_range+1):
            possible_targets.append(players[i])
        possible_targets.remove(self.active_player)
        return possible_targets

    def use_card(self, card, target=None):
        if isinstance(card, Cards.PangCard):
            if isinstance(target, Player):
                if target in self.get_possible_targets():
                    logging.info('Using pang! on {}'.format(target))
                    self.active_player.remove_card(card)
                    if self.use_barrel(target):
                        return True
                    if self.use_miss_card(target):
                        return True
                    target.change_health(-1)
                else:
                    raise InvalidTargetException('Target {} is out of range.'.format(target))
            else:
                raise InvalidTargetException('Target {} is not a valid target'.format(target))
        elif isinstance(card, Cards.MissCard):
            if isinstance(target, Player):
                self.active_player.remove_card(card)
                # TODO create miss card trigger
                logging.info('Using miss card')

        elif isinstance(card, Cards.DrawCard):
            logging.info('Using card {}, adding {} cards to hand.'.format(card, card.draw_amount))
            self.active_player.add_cards(self.deck.take_top_card(amount=card.draw_amount))
            self.active_player.remove_card(card)
        elif isinstance(card, Cards.EquipmentCard):
            logging.info('Equipping {}, with ability to {}'.format(card, card.ability))
            self.active_player.equipment = card
            self.active_player.remove_card(card)

        elif isinstance(card, Cards.WeaponCard):
            logging.info('Equipping {}, setting range to {}'.format(card, card.weapon_range))
            self.active_player.weapon = card
            self.active_player.remove_card(card)

    def use_miss_card(self, target):
        for card in target.hand:
            if isinstance(card, Cards.MissCard):
                target.remove_card(card)
                return True
        return False

    def use_barrel(self, target):
        if isinstance(target.equipment, Cards.BarrelCard):
            barrel_card = self.deck.take_top_card()
            if barrel_card.suit == Cards.Suit.HEARTS:
                return True
        else:
            return False

class Roles(enum.Enum):
    """
    Enum representing each suit.
    """

    SHERIFF = 'Sheriff'
    OUTLAW = 'Outlaw'
    RENEGADE = 'Renegade'
    DEPUTY = 'Deputy'


class InvalidTargetException(Exception):
    pass
