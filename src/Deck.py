import src.Cards as Cards
from src.Cards import Suit
import random


class StandardDeck:
    """
    Represents a deck of cards. Creates a deck standard deck of 52 unsorted cards.
    """

    def __init__(self, discard_pile=False):
        self.deck_of_cards = self.create_deck(discard_pile)
        self.shuffle_card()

    def __str__(self):
        return "{}".format([str(card) for card in self.deck_of_cards])

    def __len__(self):
        return len(self.deck_of_cards)

    def create_deck(self, discard_pile):
        """
        Create all the different cards an place in deck
        :return:
        """
        deck = []
        if not discard_pile:
            for s in Suit:
                for i in range(2, 9):
                    deck.append(Cards.PangCard(i, s))
            return deck
        else:
            return deck

    def take_top_card(self, reshuffle=True):
        """
        Returns top card and removes from deck.

        :return: TopCard
        """
        if len(self.deck_of_cards) == 0:
            if reshuffle:
                self.deck_of_cards = self.create_deck()
            else:
                raise EmptyDeckError()
        return self.deck_of_cards.pop()

    def put_card_on_top(self, card):
        """
        Put a card on the top of the deck. Used for playing cards and adding it to discard pile
        :param card: The played card
        :return:
        """
        self.deck_of_cards.append(card)

    def shuffle_card(self):
        """
        Shuffles the deck of cards
        """
        random.shuffle(self.deck_of_cards)


class EmptyDeckError(Exception):
    pass
