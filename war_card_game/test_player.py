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
        test_player = player.Player("Player1")

        # act

        # assert
        self.assertEqual(0, len(test_player.hand))

    def test_of_add_card(self):
        '''
        add card test
        '''

        # arrange
        test_player = player.Player("Player1")

        # act
        test_player.add_cards(card.Card(card.suits[0], card.ranks[0]))

        # assert
        self.assertEqual(1, len(test_player.hand))

    def test_of_add_cards(self):
        '''
        add cards test
        '''

        # arrange
        test_player = player.Player("Player1")

        # act
        test_cards = [
            card.Card(card.suits[0], card.ranks[0]),
            card.Card(card.suits[0], card.ranks[1])]
        test_player.add_cards(test_cards)

        # assert
        self.assertEqual(2, len(test_player.hand))

    def test_of_play_card(self):
        '''
        play card test
        '''

        # arrange
        test_player = player.Player("Player1")
        test_cards = [
            card.Card(card.suits[0], card.ranks[0]),
            card.Card(card.suits[0], card.ranks[1])]
        test_player.add_cards(test_cards)

        # act
        test_card = test_player.play_card()

        # assert
        self.assertEqual(1, len(test_player.hand))
        self.assertEqual("Two of Hearts", str(test_card)
)

if __name__ == "__main__":
    unittest.main()
