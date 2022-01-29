import time

class Prediction():

    def __init__(self,data,knn):
        self.data = data
        self.knn = knn
        self.threshold = 70
        self.test_size = 500

    def predict(self,train_size,image_num, k_value):

        train_labels = self.data.train_labels[:train_size]

        #transform pixels from range 0-255 to 0,1 where 0 is white 1 is black
        train_set, test_set = self.data.boolean_data(self.data.train_images[:train_size],self.data.test_images[:self.test_size],self.threshold)

        test = test_set[image_num]
        prediction = self.knn.k_nearest_neighbours(test,train_set,k_value)

        result = {}
        for i in prediction:
            if int(train_labels[i[1]]) not in result:
                result[int(train_labels[i[1]])] = 1
            else:
                result[int(train_labels[i[1]])] += 1

        ret = max(result)
        print("image to predict: ", self.data.test_labels[image_num], ", Predicted: ", ret)
        return ret


    def accuracy_test(self,train_size, k_value):

        train_labels = self.data.train_labels[:train_size]
        test_labels = self.data.test_labels[:self.test_size]

        #shape from 1d arrays back to 28x28 images
        train_set,test = self.data.shape_self.data(self.data.train_images[:train_size],self.data.test_images[:self.test_size])

        #transform pixels from range 0-255 to 0,1 where 0 is white 1 is black
        self.data.boolean_self.data(train_set,test,self.threshold)

        correct = 0
        start = time.time()
        for a in range(len(test)):
            print(a,"/",len(test), end="\r")

            image_test = test[a]
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
        accuracy = (correct/len(test))*100
        print("Accuracy: ", accuracy, " % ")

        return accuracy
