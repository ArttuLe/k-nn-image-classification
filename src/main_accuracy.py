import time

from knn import KNN
from prediction import Prediction
from data import Data



def main_accuracy():

    knn = KNN()
    prediction = Prediction(knn)
    data = Data()

    train_size = input("Input training set size: ")
    test_size = input("Input testing set size: ")
    k_value = input("Input the K value: ")

    k_value = int(k_value)

    #Load the correct amount of data from the Data class
    train_set = data.train[:int(train_size)]
    train_labels = data.train_labels[:int(train_size)]

    test_set = data.test[:int(test_size)]
    test_labels = data.test_labels[:int(test_size)]

    start = time.time()
    correct = 0

    #Run the prediction on the test set and calculate the accuracy

    for a in range(len(test_set)):

        image = test_set[a]
        test_label = test_labels[a]

        prediction = knn.k_nearest_neighbours(image,train_set,k_value)

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
    accuracy = (correct/len(test_set))*100
    print("Accuracy: ", accuracy, " % ", " k value: ", k_value)

if __name__ == "__main__":
    main_accuracy()
