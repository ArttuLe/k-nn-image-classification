import time

class Prediction():

    def __init__(self,knn):
        self.knn = knn
        self.threshold = 70
        self.test_size = 500

    def predict(self,train_set, train_labels, test_image, k_value):

        prediction = self.knn.k_nearest_neighbours(test_image,train_set,k_value)

        result = {}
        for i in prediction:
            if int(train_labels[i[1]]) not in result:
                result[int(train_labels[i[1]])] = 1
            else:
                result[int(train_labels[i[1]])] += 1

        ret = max(result)

        return ret


    def accuracy_test(self,train_set, train_labels, test_set, test_labels, k_value):

        correct = 0
        start = time.time()
        for a in range(len(test_set)):

            image_test = test_set[a]
            test_label = test_labels[a]

            prediction = self.knn.k_nearest_neighbours(image_test,train_set,k_value)

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
        print("Accuracy: ", accuracy, " % ")

        return accuracy
