import unittest
from data import Data

class TestData(unittest.TestCase):

    def test_load_data(self):
        data = Data()

        length = len(data.train_images)

        self.assertEqual(length,60000)