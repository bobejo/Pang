import unittest
import src.Cards as cards


class TestCards(unittest.TestCase):

    def test_card_attributes(self):
        card = cards.Card('test_card', cards.Suit.HEARTS, 5, cards.CardPosition.TARGET)
        self.assertEqual(card.name, 'test_card')
        self.assertEqual(card.value, 5)
        self.assertEqual(card.suit, cards.Suit.HEARTS)
        self.assertEqual(card.card_position, cards.CardPosition.TARGET)

    def test_card_instances(self):
        pang_card = cards.PangCard(cards.Suit.HEARTS, 5)
        rifle_card = cards.RifleCard(cards.Suit.SPADES, 2)
        horse_card = cards.HorseCard(cards.Suit.DIAMONDS, 8)

        self.assertIsInstance(pang_card, cards.Card)
        self.assertIsInstance(rifle_card, cards.Card)
        self.assertIsInstance(rifle_card, cards.WeaponCard)
        self.assertIsInstance(horse_card, cards.Card)
        self.assertIsInstance(horse_card, cards.EquipmentCard)

    def test_card_names(self):
        pang_card = cards.PangCard(cards.Suit.HEARTS, 5)
        rifle_card = cards.RifleCard(cards.Suit.SPADES, 2)
        horse_card = cards.HorseCard(cards.Suit.DIAMONDS, 8)
        self.assertEqual(pang_card.name, cards.CardName.PANG)
        self.assertEqual(rifle_card.name, cards.CardName.RIFLE)
        self.assertEqual(horse_card.name, cards.CardName.HORSE)
