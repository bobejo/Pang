import unittest
import src.Cards as Cards


class TestCards(unittest.TestCase):

    def test_card_attributes(self):
        card = Cards.Card('test_card', Cards.Suit.HEARTS, 5, Cards.CardPosition.TARGET)
        self.assertEqual(card.name, 'test_card')
        self.assertEqual(card.value, 5)
        self.assertEqual(card.suit, Cards.Suit.HEARTS)
        self.assertEqual(card.card_position, Cards.CardPosition.TARGET)

    def test_card_instances(self):
        pang_card = Cards.PangCard(Cards.Suit.HEARTS, 5)
        rifle_card = Cards.RifleCard(Cards.Suit.SPADES, 2)
        horse_card = Cards.HorseCard(Cards.Suit.DIAMONDS, 8)

        self.assertIsInstance(pang_card, Cards.Card)
        self.assertIsInstance(rifle_card, Cards.Card)
        self.assertIsInstance(rifle_card, Cards.WeaponCard)
        self.assertIsInstance(horse_card, Cards.Card)
        self.assertIsInstance(horse_card, Cards.EquipmentCard)

    def test_card_names(self):
        pang_card = Cards.PangCard(Cards.Suit.HEARTS, 5)
        rifle_card = Cards.RifleCard(Cards.Suit.SPADES, 2)
        horse_card = Cards.HorseCard(Cards.Suit.DIAMONDS, 8)
        self.assertEqual(pang_card.name, Cards.CardName.PANG)
        self.assertEqual(rifle_card.name, Cards.CardName.RIFLE)
        self.assertEqual(horse_card.name, Cards.CardName.HORSE)

    def test_card_str(self):
        pang_card = Cards.PangCard(Cards.Suit.HEARTS, 5)
        rifle_card = Cards.RifleCard(Cards.Suit.SPADES, 2)
        horse_card = Cards.HorseCard(Cards.Suit.DIAMONDS, 8)
        pass
