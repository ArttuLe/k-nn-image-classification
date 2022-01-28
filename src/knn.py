from heapq import heappush,heappop,heapify
from distance import Distance

class KNN():

    def k_nearest_neighbours(test_image, train_set, k):

        neighbours = []
        heapify(neighbours)

        for i in range(len(train_set)):
            print(int((i/len(train_set)*100)), "%", end="\r")
            dist = Distance().calculate_distances(test_image,train_set[i])
            heappush(neighbours,(dist,i))

        prediction = []
        for i in range(k):
            prediction.append(heappop(neighbours))

        return prediction
