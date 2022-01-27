import numpy as np
from matplotlib import pyplot as plt

from data import Data
from knn import KNN
from distance import Distance


def main():
    
    data = Data()

    threshold = 70
    train_size = 100
    test_size = 20

    train_labels = data.train_labels[:train_size]
    test_labels = data.test_labels[:test_size]

    #shape from 1d array back to 28x28 images
    train,test = data.shape_data(data.train_images[:train_size],data.test_images[:test_size])

    #transform pixels from range 0-255 to 0,1 where 0 is white 1 is black
    train_bool,test_bool = data.boolean_data(train,test,threshold)
    image_test = test[5]
    image_train = train[6]
    Distance().calculate_distances(image_test,image_train)
    
    #plt.imshow(image_train, interpolation='none')
    #plt.title(int(train_labels[6]))
    #plt.show()
    #plt.imshow(image_test, interpolation='none')
    #plt.title(int(test_labels[5]))
    #plt.show()
    





if __name__ == "__main__":
    main()