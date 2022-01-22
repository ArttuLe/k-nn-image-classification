from heapq import heapify, heappush, heappop
from distance import Distance

class KNN():

    def calculate_distances(image_to_predict,images):

        distances = []

        for image in images:
            distances.append(Distance.euclidean_distance(image_to_predict,image))

        return distances


    #Calculate the euclidean distances against the test data and pick the k nearest neighbours
    def k_nearest_neighbours(image_to_predict,k,distances):

        indexes = []
        heapify(indexes)

        
        for i in range(len(distances)):
            if len(indexes) < k:
                heappush(indexes,i)
            elif distances[i] < distances[indexes[0]] and len(indexes) >= k:
                heappop(indexes)
                heappush(indexes, i)

        return indexes

    def cross_validation():
        pass





