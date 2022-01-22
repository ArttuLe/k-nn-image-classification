from data import Data
from knn import KNN
from matplotlib import pyplot as plt
import numpy as np


def main():
    
    data = Data()

    correct = 0
    n = 10
    predict = data.test_images[0]
    num = data.test_labels[0]

    dist = KNN.calculate_distances(predict,data.train_images[:600])

    indexes = KNN.k_nearest_neighbours(2,dist)

    k_nn = {}
    for j in indexes:
        if int(data.train_labels[j]) not in k_nn:
            k_nn[int(data.train_labels[j])] = 1
        else:
            k_nn[int(data.train_labels[j])] += 1

    prediction = max(k_nn, key=k_nn.get)

    print("Real num: ",num ," prediction: ",prediction)
    if prediction == num:
        correct += 1

        #image = np.array(predict)
        #image = image.reshape(28,28)

        #plt.imshow(image)
        #plt.title(('Prediction: {}').format(prediction))
        #plt.show()

    print("Accuracy: ",(correct/n)*100," %")
    





if __name__ == "__main__":
    main()