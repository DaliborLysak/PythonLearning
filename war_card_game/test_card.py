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
        self.assertEqual(13, test_card.value)

if __name__ == "__main__":
    unittest.main()
