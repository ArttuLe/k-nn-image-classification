import numpy as np
import math



class Distance():

    def euclidean_distance(image1,image2):

        dist = 0
        for i in range(784):
            dist += (image1[i]-image2[i])**2
        return np.sqrt(dist)

    def hausdorff_modified_distance(self):
        pass
