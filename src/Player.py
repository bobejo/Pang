import logging
from src.Cards import BeerCard

class Player:
    def __init__(self, name, role, character):
        self.name = name
        self.role = role
        self.character = character
        self.hand = []
        self.health = self.get_start_health()
        self.weapon = None
        self.equipment = None

    def add_card(self, card):
        self.hand.append(card)

    def change_health(self, value):
        self.health += value
        if self.health < 0:
            if self.has_beer():
                logging.info('Player {} has {} life and need to drink beer')
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


class PlayerDeadException(Exception):
    pass
