import unittest
import tic_tac_toe

class TestOccupied(unittest.TestCase):

    def test_isnot_occupied(self):
        # arrange
        allowed_coordinates = range(1,10)
        active_game = {}
        for i in allowed_coordinates:
             active_game[i] = " "

        # act
        is_occupied = tic_tac_toe.occupied(active_game, 1)

        # assert
        self.assertFalse(is_occupied)

if __name__ == "__main__":
    unittest.main()