import logging
import enum
from src.Cards import BeerCard


log = logging.getLogger(__name__)

class Player:
    def __init__(self, name, role, character):
        self.name = name
        self.role = role
        self.character = character
        self.hand = []
        self.health = self.get_start_health()
        self.weapon = None
        self.equipment = None

    def __str__(self):
        return 'Player {}'.format(self.name)

    def add_cards(self, cards):
        for card in cards:
            self.hand.append(card)

    def remove_card(self, card, deck=None):
        if deck:
            deck.discard_pile.append(card)
        self.hand.remove(card)

    def change_health(self, value):
        self.health += value
        if self.health < 1:
            if self.has_beer():
                log.info('Player {} has {} life and need to drink beer')
                beer_card = self.get_beer()
                self.hand.remove(beer_card)
                self.change_health(1)
            else:
                raise PlayerDeadException('Player {} is DEAD. Player was role {}'.format(self.name, self.role))

    def has_beer(self):
        if self.get_beer():
            return True
        else:
            return False

    def get_beer(self):
        for card in self.hand:
            if isinstance(card, BeerCard):
                return card
        return None

    def get_start_health(self):
        return self.character.health


class Roles(enum.Enum):
    """
    Enum representing each suit.
    """

    SHERIFF = 'Sheriff'
    OUTLAW = 'Outlaw'
    RENEGADE = 'Renegade'
    DEPUTY = 'Deputy'


class PlayerDeadException(Exception):
    pass
