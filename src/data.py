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


    def shape_data(self,train_data,test_data):

        train_data = train_data.reshape(len(train_data),28,28)
        test_data = test_data.reshape(len(test_data),28,28)

        print("Training set: ", train_data.shape)
        print("Testing set: ", test_data.shape)

        return train_data,test_data

    def boolean_data(self, train_data, test_data, threshold):


        for a in range(len(train_data)):
            for i in range(28):
                for j in range(28):
                    if train_data[a][i][j] < threshold:
                        train_data[a][i][j] = 0
                    elif train_data[a][i][j] >= threshold:
                        train_data[a][i][j] = 1
        print("Training data done...")

        for a in range(len(test_data)):
            for i in range(28):
                for j in range(28):
                    if test_data[a][i][j] < threshold:
                        test_data[a][i][j] = 0
                    elif test_data[a][i][j] >= threshold:
                        test_data[a][i][j] = 1
        print("Test data done...")

        return train_data, test_data