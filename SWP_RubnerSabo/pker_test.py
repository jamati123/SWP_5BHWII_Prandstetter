import unittest
from Pker import set_deck, draw_cards, draw_hand, set_range, order, royal_flush, determine_combination

class TestPker(unittest.TestCase):

    def test_set_deck(self):
        deck = set_deck()
        self.assertEqual(len(deck), 52)
        self.assertIn(('Kreuz', '2'), deck)
        self.assertIn(('Herz', 'Ass'), deck)

    def test_draw_cards(self):
        deck = set_deck()
        card = draw_cards(deck)
        self.assertEqual(len(deck), 51)
        self.assertNotIn(card, deck)

    def test_draw_hand(self):
        deck = set_deck()
        hand = draw_hand(deck)
        self.assertEqual(len(hand), 5)
        for card in hand:
            self.assertNotIn(card, deck)

    def test_set_range(self):
        self.assertEqual(set_range('2'), 0)
        self.assertEqual(set_range('Ass'), 12)

    def test_order(self):
        hand = [('Kreuz', 'Ass'), ('Pik', '2'), ('Herz', 'König')]
        ordered_hand = order(hand)
        self.assertEqual(ordered_hand, [('Pik', '2'), ('Herz', 'König'), ('Kreuz', 'Ass')])

    def test_royal_flush(self):
        hand = [('Kreuz', '10'), ('Kreuz', 'Bube'), ('Kreuz', 'Dame'), ('Kreuz', 'König'), ('Kreuz', 'Ass')]
        self.assertTrue(royal_flush(hand))
        hand = [('Kreuz', '10'), ('Kreuz', 'Bube'), ('Kreuz', 'Dame'), ('Kreuz', 'König'), ('Pik', 'Ass')]
        self.assertFalse(royal_flush(hand))

    def test_determine_combination(self):
        hand = [('Kreuz', '10'), ('Kreuz', 'Bube'), ('Kreuz', 'Dame'), ('Kreuz', 'König'), ('Kreuz', 'Ass')]
        self.assertEqual(determine_combination(hand), "Royal Flush")
        hand = [('Kreuz', '9'), ('Kreuz', '10'), ('Kreuz', 'Bube'), ('Kreuz', 'Dame'), ('Kreuz', 'König')]
        self.assertEqual(determine_combination(hand), "Straight Flush")
        hand = [('Kreuz', '9'), ('Kreuz', '9'), ('Kreuz', '9'), ('Kreuz', '9'), ('Kreuz', 'König')]
        self.assertEqual(determine_combination(hand), "Four of a Kind")
        hand = [('Kreuz', '9'), ('Kreuz', '9'), ('Kreuz', '9'), ('Kreuz', 'König'), ('Kreuz', 'König')]
        self.assertEqual(determine_combination(hand), "Full House")
        hand = [('Kreuz', '2'), ('Kreuz', '4'), ('Kreuz', '6'), ('Kreuz', '8'), ('Kreuz', '10')]
        self.assertEqual(determine_combination(hand), "Flush")
        hand = [('Kreuz', '2'), ('Pik', '3'), ('Herz', '4'), ('Karo', '5'), ('Kreuz', '6')]
        self.assertEqual(determine_combination(hand), "Straight")
        hand = [('Kreuz', '9'), ('Pik', '9'), ('Herz', '9'), ('Karo', 'König'), ('Kreuz', 'Ass')]
        self.assertEqual(determine_combination(hand), "Three of a Kind")
        hand = [('Kreuz', '9'), ('Pik', '9'), ('Herz', 'König'), ('Karo', 'König'), ('Kreuz', 'Ass')]
        self.assertEqual(determine_combination(hand), "Two Pair")
        hand = [('Kreuz', '9'), ('Pik', '9'), ('Herz', 'König'), ('Karo', 'Ass'), ('Kreuz', '2')]
        self.assertEqual(determine_combination(hand), "One Pair")
        hand = [('Kreuz', '2'), ('Pik', '4'), ('Herz', '6'), ('Karo', '8'), ('Kreuz', '10')]
        self.assertEqual(determine_combination(hand), "High Card")

if __name__ == '__main__':
    unittest.main()