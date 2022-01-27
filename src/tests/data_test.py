import unittest
from data import Data

class TestData(unittest.TestCase):

    def test_load_data(self):
        data = Data()

        length = len(data.train_images)

        self.assertEqual(length,60000)

    def test_shape_data(self):

        data = Data()

        train,test = data.shape_data(data.train_images,data.test_images)

        self.assertEqual(train.shape, (60000, 28, 28))
        self.assertEqual(test.shape, (10000, 28, 28))