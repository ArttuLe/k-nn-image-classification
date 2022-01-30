import unittest
import numpy as np

from distance import Distance

class TestDistance(unittest.TestCase):

    def test_calculate_distances(self):

        num = np.array([[0,0,1,0],
                        [0,0,1,0],
                        [0,0,1,0],
                        [0,0,1,0]])

        test_coordinates = Distance().get_black_pixels(num)
        distances = Distance().calculate_distances(test_coordinates,num)

        self.assertEqual(distances,0)

    def test_distance(self):

        num = np.array([[0,0,1,0],
                        [0,0,1,0],
                        [0,0,1,0],
                        [0,0,1,0]])

        test_coordinates = Distance().get_black_pixels(num)
        distance = Distance().distance(test_coordinates[0],test_coordinates)

        self.assertEqual(distance,0)