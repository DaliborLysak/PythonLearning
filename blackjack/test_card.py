'''
War card game - Card - unit tests
'''

import unittest
import card

class TestCard(unittest.TestCase):
    '''
    Test suit for card
    '''

    def test_of_creation(self):
        '''
        creation test
        '''

        # arrange
        test_card = card.Card("Hearts", "King")

        # act
        actual_str = str(test_card)

        # assert
        self.assertEqual("King of Hearts", actual_str)
        self.assertEqual(10, test_card.value)

    def test_of_values(self):
        '''
        test of values
        '''

        # arrange
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        test_cards = []
        test_cards.append(card.Card("Hearts", "Two"))
        test_cards.append(card.Card("Hearts", "Three"))
        test_cards.append(card.Card("Hearts", "Four"))
        test_cards.append(card.Card("Hearts", "Five"))
        test_cards.append(card.Card("Hearts", "Six"))
        test_cards.append(card.Card("Hearts", "Seven"))
        test_cards.append(card.Card("Hearts", "Eight"))
        test_cards.append(card.Card("Hearts", "Nine"))
        test_cards.append(card.Card("Hearts", "Ten"))
        test_cards.append(card.Card("Hearts", "Jack"))
        test_cards.append(card.Card("Hearts", "Queen"))
        test_cards.append(card.Card("Hearts", "King"))
        test_cards.append(card.Card("Hearts", "Ace"))

        # act
        actual_values = list(map(lambda x: x.value, test_cards))

        # assert
        self.assertListEqual(list(values), actual_values)

if __name__ == "__main__":
    unittest.main()
