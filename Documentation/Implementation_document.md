
## Implementation of the project


### General structure of the project

The project consists of three parts. The first part being all the data related functionalities, second being all the calculations regarding the distances between pixels in the images and the third being the prediction.

Data is being processed slightly before the actual application starts. Pre-processing includes Re-shaping the images from a 1-d arrays back to 2-d 28x28 sized images for the calculations to work correctly. Then the images are converted into boolean type images by converting pixel values into 0's or 1's based on a threshold value given. For example if a threshold value is 70 and a pixel has value 32, it is converted into 0, and if a pixel has value 234 it is converted to 1. This boolean type image data is then used in the calculations.







### Big-O analysis

The Time complexity of the application is O(A*B), and the space complexity being the same. A is the size of the training set used in the prediction, and B is the size of the testing set being used.

You can immediatly see from the complexities that the algorithm will not be great with large datasets, as the space needed will go up significantly as will the time it takes to process all the data.


### Accuracy and performance of the algorithm

The accuracy of the application is highly dependant on the size of the data being used, as it generally performs better when coupled with a bigger training set.


### Possible improvements

Improve the algorithm and the time it takes to finish computation on a single image in order to test on bigger datasets.

Improve the UI of the program.

Implement different distance calculations to compare the accuracy.



### Sources

See the Project definition document.