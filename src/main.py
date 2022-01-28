import numpy as np
from matplotlib import pyplot as plt

from data import Data
from knn import KNN
from distance import Distance


def main():
    
    data = Data()

    threshold = 70
    train_size = 1000
    test_size = 10

    train_labels = data.train_labels[:train_size]
    test_labels = data.test_labels[:test_size]

    #shape from 1d array back to 28x28 images
    train_set,test = data.shape_data(data.train_images[:train_size],data.test_images[:test_size])

    #transform pixels from range 0-255 to 0,1 where 0 is white 1 is black
    data.boolean_data(train_set,test,threshold)

    for a in range(len(test)):
        print(a)
        correct = 0
        image_test = test[a]
        test_label = test_labels[a]

        prediction = KNN.k_nearest_neighbours(image_test,train_set,3)

        result = {}
        for i in prediction:
            print(train_labels[i[1]], ", distance: ",i[0])

            if int(train_labels[i[1]]) not in result:
                result[int(train_labels[i[1]])] = 1
            else:
                result[int(train_labels[i[1]])] += 1

        #print("Prediction: ",max(result))
        #print("Correct number: ", test_label)
        if max(result) == int(test_label):
            print("Correct")
            correct += 1

    print("Accuracy: ", ((correct//len(test))*100), "% ")

    





if __name__ == "__main__":
    main()