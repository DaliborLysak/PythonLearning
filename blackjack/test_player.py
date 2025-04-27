'''
War card game - Player - unit tests
'''

import unittest
import player
import card

class TestCard(unittest.TestCase):
    '''
    Test suit for deck
    '''

    def test_of_creation(self):
        '''
        creation test
        '''

        # arrange
        test_player = player.Player("Player")

        # act

        # assert
        self.assertEqual(0, len(test_player.hand))

    def test_of_add_card(self):
        '''
        add card test
        '''

        # arrange
        test_player = player.Player("Player")

        # act
        test_player.add_card(card.Card(card.suits[0], card.ranks[0]))

        # assert
        self.assertEqual(1, len(test_player.hand))

if __name__ == "__main__":
    unittest.main()
