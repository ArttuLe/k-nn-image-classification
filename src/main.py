import numpy as np
import time
from matplotlib import pyplot as plt


from data import Data
from knn import KNN
from distance import Distance


def main():
    
    data = Data()

    threshold = 70
    train_size = 10000
    test_size = 25

    train_labels = data.train_labels[:train_size]
    test_labels = data.test_labels[:test_size]

    #shape from 1d arrays back to 28x28 images
    train_set,test = data.shape_data(data.train_images[:train_size],data.test_images[:test_size])

    #transform pixels from range 0-255 to 0,1 where 0 is white 1 is black
    data.boolean_data(train_set,test,threshold)

    correct = 0
    start = time.time()
    for a in range(len(test)):
        print(a,"/",len(test), end="\r")

        image_test = test[a]
        test_label = test_labels[a]

        prediction = KNN.k_nearest_neighbours(image_test,train_set,3)

        result = {}
        for i in prediction:
            if int(train_labels[i[1]]) not in result:
                result[int(train_labels[i[1]])] = 1
            else:
                result[int(train_labels[i[1]])] += 1

        if max(result) == int(test_label):
            correct += 1

    elapsed_time = time.time()-start
    print(elapsed_time," Seconds.")

    print("Accuracy: ", (correct/len(test))*100, " % ")

    





if __name__ == "__main__":
    main()