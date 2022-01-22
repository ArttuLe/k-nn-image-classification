import numpy as np
import pandas as pd

class Data():

    #Loads the data from csv files into numpy arrays
    def __init__(self):
        self.train_images = pd.read_csv('data/images.csv', header=None)
        self.train_labels = pd.read_csv('data/labels.csv', header=None)

        self.test_images = pd.read_csv('data/test_images.csv', header=None)
        self.test_labels = pd.read_csv('data/test_labels.csv', header=None)

        self.train_images = self.train_images.to_numpy()
        self.train_labels = self.train_labels.to_numpy()

        self.test_images = self.test_images.to_numpy()
        self.test_labels = self.test_labels.to_numpy()


        