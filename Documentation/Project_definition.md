# Project definition

-The aim for this project is to detect the hand written digits of the [MNIST](http://yann.lecun.com/exdb/mnist/)-database correctly using the [k-nearest neighbours method](http://scholarpedia.org/article/K-nearest_neighbor).

## Data structures and algorithms used in the project

-The k-nearest neighbours algorithm
-K-fold cross validation algorithm
-Heap data structure for keeping up with the k-nearest neighbours

## Time and Space complexities of the algorithm

-Space complexity for the k-neareset neighbours algorithm would be O(A*B), where A is the amount of images used for training, and B is the amount of features in a single image, which in this case, means the number of pixels in a single image.

-Time complexity for the algorithm will also be O(A*B), since the algorithm needs to go through all the images pixel by pixel to calculate the distances for each image. Runtime complexity will be O(A*B*K), where K is the number of nearest neighbours.

## How does the application work

The algorithm receives hand written digits from the MNIST-database as input, where the images are flattened from the original 28x28 size to a single 1-dimensional array of 784 pixels. The algorithm then calculates the distances (Euclidean, Modified Hausdorff etc.) of the test image against all of the images in the training set and stores the distances. From the distances the algorithm then picks the K-nearest neighbours and detects the test image as the number with the most members in the k-nearest neighbours set. For example if the k-nearest neighbours are numbers 2,3,3, the algorithm then detects the test image as number 3.

## Other information

-The project will be done in python, but for peer-review purposes C/C++ -projects can also be reviewed.
-Study Track: Tietojenkäsittelytieteen kandidaatti
-Language for the project: English

## Sources

-[Modified Hausdorff distance for object matching](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.1.8155&rank=5&q=hausdorff&osm=&ossid=)
-[K-Nearest Neighbour](http://scholarpedia.org/article/K-nearest_neighbor)
-[Comparing images using the Hausdorff distance](https://people.eecs.berkeley.edu/~malik/cs294/Huttenlocher93.pdf)
-[Euclidean distance](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.680.2097&rep=rep1&type=pdf)
More to come...
