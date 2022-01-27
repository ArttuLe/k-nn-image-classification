import numpy as np




class Distance():

    #closest pixel for a in B
    def distance(self,point, point_set_B):
        j = point[1]
        i = point[0]
        print(i,",", j)
        print(point_set_B)
        

        
    
    #sum of distances for every pixel in A to B
    def calculate_distances(self,image_test,image_train):

        sum_a = 0
        sum_b = 0
        test_coordinates = self.get_black_pixels(image_test)
        train_coordinates = self.get_black_pixels(image_train)

        #sum for every a in A for B
        for coord in test_coordinates:
            sum_a += self.distance(coord,train_coordinates)

        #sum for every b in B for A
        for coord in train_coordinates:
            sum_b += self.distance(coord,test_coordinates)

        sum = sum_a+sum_b

        return print(sum)


    #get coordinates for pixels that are black in an image.
    def get_black_pixels(self, image):

        coordinates = []

        for i in range(len(image)):
            for j in range(len(image)):
                if image[i][j] == 1:
                    coordinates.append((i,j))

        return coordinates



#if image[i][j] == True:
#            dist = 0
#            return dist
#        if image[i-1][j] == True:
#            dist = 1
#            return dist
#        if image[i+1][j] == True:
#            dist = 1
#            return dist
#        if image[i][j-1] == True:
#            dist = 1
#            return dist
#        if image[i][j+1] == True:
#            dist = 1
#            return dist
#        if image[i-1][j-1] == True:
#            dist = np.sqrt(2)
#            return dist
#        if image[i+1][j+1] == True:
#            dist = np.sqrt(2)
#            return dist
#        if image[i+1][j-1] == True:
#            dist = np.sqrt(2)
#            return dist
#        if image[i-1][j+1] == True:
#            dist = np.sqrt(2)
#            return dist
#        else:
#            return
