from heapq import heappush,heappop,heapify
from distance import Distance

class KNN():

    def k_nearest_neighbours(self,test_image, train_set, k):

        neighbours = []
        heapify(neighbours)
        test_coordinates = Distance().get_black_pixels(test_image)

        for i in range(len(train_set)):
            dist = Distance().calculate_distances(test_coordinates,train_set[i])
            heappush(neighbours,(dist,i))

        prediction = []
        for i in range(k):
            prediction.append(heappop(neighbours))

        return prediction
