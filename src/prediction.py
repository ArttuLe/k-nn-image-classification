
class Prediction():

    def __init__(self,knn):
        self.knn = knn

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
