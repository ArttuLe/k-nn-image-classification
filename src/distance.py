import numpy as np
from heapq import heappush,heappop,heapify




class Distance():

    #closest pixel for point a in pointset B
    def distance(self,point, point_set_B):
        j = point[1]
        i = point[0]

        distances = []
        heapify(distances)

        for b in point_set_B:
            dist = np.sqrt(((b[0]-i)**2) + ((b[1]-j)**2))
            heappush(distances,dist)
        closest = heappop(distances)

        return closest
        

    #sum of distances for every pixel in A to B
    def calculate_distances(self,image_test,image_train):

        sum_a = 0
        sum_b = 0
        test_coordinates = image_test
        train_coordinates = self.get_black_pixels(image_train)

        #sum for every a in A for B
        for coord in test_coordinates:
            sum_a += self.distance(coord,train_coordinates)

        #sum for every b in B for A
        for coord in train_coordinates:
            sum_b += self.distance(coord,test_coordinates)

        sum = sum_a+sum_b

        return sum


    #get coordinates for pixels that are black in an image.
    def get_black_pixels(self, image):

        coordinates = []

        for i in range(len(image)):
            for j in range(len(image)):
                if image[i][j] == 1:
                    coordinates.append((i,j))

        return coordinates