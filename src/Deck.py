import src.Cards as Cards
import random


class StandardDeck:
    """
    Represents a deck of cards. Creates a deck standard deck of 52 unsorted cards.
    """

    def __init__(self):
        self.deck_of_cards = self.create_deck()

    def __eq__(self, other):
        self.deck_of_cards == other.deck_of_cards

    def __str__(self):
        return "{}".format([str(card) for card in self.deck_of_cards])

    def __len__(self):
        return len(self.deck_of_cards)

    def create_deck(self):
        deck = []
        suits = [Cards.Suit.HEARTS, Cards.Suit.SPADES, Cards.Suit.DIAMONDS, Cards.Suit.CLUBS]

        for s in suits:
            for i in range(2, 9):
                deck.append(Cards.Card(i, s))

        self.shuffle_card()

        return deck

    def take_top_card(self,reshuffle=True):
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

    def shuffle_card(self):
        """
        Shuffles the deck of cards
        """
        random.shuffle(self.deck_of_cards)


class EmptyDeckError(Exception):
    pass
