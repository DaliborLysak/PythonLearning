'''
War card game - Deck - unit tests
'''

import unittest
import deck

class TestCard(unittest.TestCase):
    '''
    Test suit for deck
    '''

    def test_of_creation(self):
        '''
        creation test
        '''

        # arrange
        test_deck = deck.Deck()

        # act

        # assert
        self.assertEqual(52, len(test_deck.cards))

    def test_of_deal_card(self):
        '''
        deal card test
        '''

        # arrange
        test_deck = deck.Deck()

        # act
        test_deck.deal_card()

        # assert
        self.assertEqual(51, len(test_deck.cards))

if __name__ == "__main__":
    unittest.main()
