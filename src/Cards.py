import enum
import abc


class Card(metaclass=abc.ABCMeta):
    def __init__(self, name, suit, value, card_position):
        self.name = name
        self.suit = suit
        self.value = value
        self.card_position = card_position


class PangCard(Card):
    def __init__(self, suit, value):
        Card.__init__(self, CardName.PANG, suit, value, card_position=CardPosition.TARGET)


class MissCard(Card):
    def __init__(self, suit, value):
        Card.__init__(self, CardName.MISS, suit, value, card_position=CardPosition.SELF)


class DrawCard(Card):
    def __init__(self, name, suit, value, draw_amount):
        Card.__init__(self, name, suit, value, card_position=CardPosition.SELF)
        self.draw_amount = draw_amount


class BeerCard(Card):
    def __init__(self, suit, value):
        Card.__init__(self, CardName.BEER, suit, value, card_position=CardPosition.SELF)


class PanikCard(Card):
    def __init__(self, suit, value):
        Card.__init__(self, CardName.PANIK, suit, value, card_position=CardPosition.TARGET)


class DestroyCard(Card):
    def __init__(self, suit, value):
        Card.__init__(self, CardName.CATBALOU, suit, value, card_position=CardPosition.TARGET)


class EquipmentCard(Card):
    def __init__(self, name, suit, value, ability):
        Card.__init__(self, name, suit, value, card_position=CardPosition.FRONT)
        self.ability = ability


class HorseCard(EquipmentCard):
    def __init__(self, suit, value):
        EquipmentCard.__init__(self, CardName.HORSE, suit, value, ability='Evasion')


class BarrelCard(EquipmentCard):
    def __init__(self, suit, value):
        EquipmentCard.__init__(self, CardName.BARREL, suit, value,ability='Block')


class ScopeCard(EquipmentCard):
    def __init__(self, suit, value):
        EquipmentCard.__init__(self, CardName.SCOPE, suit, value,ability='Range')


class WeaponCard(Card):
    def __init__(self, name, suit, value, weapon_range):
        Card.__init__(self, name, suit, value, card_position=CardPosition.FRONT)
        self.weapon_range = weapon_range


class RifleCard(WeaponCard):
    def __init__(self, suit, value):
        WeaponCard.__init__(self, CardName.RIFLE, suit, value, weapon_range=3)


class PistolCard(WeaponCard):
    def __init__(self, suit, value):
        WeaponCard.__init__(self, CardName.PISTOL, suit, value, weapon_range=2)


class CardPosition(enum.Enum):
    """
    Enum representing each card type
    """
    TARGET = "Target"
    SELF = "Self"
    All = 'All'
    FRONT = "Front"


class CardName(enum.Enum):
    """
    Enum representing each card name
    """
    PANG = "Pang"
    MISS = 'Miss'
    BEER = 'Beer'
    CATBALOU = "Catbalou"
    PANIK = "Panik"
    GATLING = 'Gatling'
    INDIANER = 'Indianer'
    VULKAN = 'Vulkan'
    PISTOL = 'Pistol'
    RIFLE = 'Rifle'
    BARREL = 'Barrel'
    HORSE = 'Horse'
    SCOPE = 'Scope'


class Suit(enum.Enum):
    """
    Enum representing each suit.
    """

    HEARTS = 0
    SPADES = 1
    DIAMONDS = 2
    CLUBS = 3

    def __str__(self):
        return '\u2661\u2660\u2662\u2663'[self.value]
