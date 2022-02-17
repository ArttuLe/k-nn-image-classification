import multiprocessing
import time
import os

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
    manager = multiprocessing.Manager()
    return_correct = manager.list()
    correct = 0

    split = int(test_size)//6
    print(split)
    #Run the prediction on the test set and calculate the accuracy

    p1 = multiprocessing.Process(target=parallel_prediction, args=(knn,train_set, train_labels,test_set[:split],test_labels[:split],k_value, return_correct))
    p2 = multiprocessing.Process(target=parallel_prediction, args=(knn,train_set, train_labels,test_set[split:split*2],test_labels[split:split*2],k_value, return_correct))
    p3 = multiprocessing.Process(target=parallel_prediction, args=(knn,train_set, train_labels,test_set[split*2:split*3],test_labels[split*2:split*3],k_value, return_correct))
    p4 = multiprocessing.Process(target=parallel_prediction, args=(knn,train_set, train_labels,test_set[split*3:split*4],test_labels[split*3:split*4],k_value, return_correct))
    p5 = multiprocessing.Process(target=parallel_prediction, args=(knn,train_set, train_labels,test_set[split*4:split*5],test_labels[split*4:split*5],k_value, return_correct))
    p6 = multiprocessing.Process(target=parallel_prediction, args=(knn,train_set, train_labels,test_set[split*5:split*6],test_labels[split*5:split*6],k_value, return_correct))
    
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()

    elapsed_time = time.time()-start
    print(elapsed_time," Seconds.")
    accuracy = (sum(return_correct)/len(test_set))*100
    print("Accuracy: ", accuracy, " % ", " k value: ", k_value)



def parallel_prediction(knn, train_set, train_labels, test_set, test_labels, k_value, return_correct):

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
            return_correct.append(1)

if __name__ == "__main__":
    #import cProfile, pstats
    #profiler = cProfile.Profile()
    #profiler.enable()
    main_accuracy()
    #profiler.disable()
    #stats = pstats.Stats(profiler).sort_stats('ncalls')
    #stats.print_stats()
