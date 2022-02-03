import pandas as pd

class Data():

    def __init__(self):
        self.train_images = pd.read_csv('data/images.csv', header=None)
        self.train_labels = pd.read_csv('data/labels.csv', header=None)

        self.test_images = pd.read_csv('data/test_images.csv', header=None)
        self.test_labels = pd.read_csv('data/test_labels.csv', header=None)

        self.train, self.test = self.process_data()

    def boolean_data(self, train_data, test_data, threshold):


        for n in range(len(train_data)):
            for i in range(28):
                for j in range(28):
                    if train_data[n][i][j] < threshold:
                        train_data[n][i][j] = 0
                    elif train_data[n][i][j] >= threshold:
                        train_data[n][i][j] = 1
        print("Training data done...")

        for n in range(len(test_data)):
            for i in range(28):
                for j in range(28):
                    if test_data[n][i][j] < threshold:
                        test_data[n][i][j] = 0
                    elif test_data[n][i][j] >= threshold:
                        test_data[n][i][j] = 1
        print("Test data done...")

        return train_data, test_data

    def process_data(self):

        self.train_images = self.train_images.to_numpy()
        self.train_labels = self.train_labels.to_numpy()
        self.test_images = self.test_images.to_numpy()
        self.test_labels = self.test_labels.to_numpy()

        self.train_images = self.train_images.reshape(len(self.train_images),28,28)
        self.test_images = self.test_images.reshape(len(self.test_images),28,28)

        self.train,self.test = self.boolean_data(self.train_images, self.test_images, 70)

        return self.train,self.test
