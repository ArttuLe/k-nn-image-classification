
## Unit Testing




### Distance metrics



### K-NN algorithm


### Manual accuracy testing

Manual accuracy testing needs to be run in order to validate the accuracy of the algorithm



Below are accuracy tests with different sized training sets and testing sets.


Train set  | test set| K-value | Accuracy |
-----------|---------|---------|----------|
10000      | 500     |  3      |    96 %  |
20000      | 1000     |  3      |    running %  |





Below tests for different k values on a small train set. Accuracy may differ with bigger train size, need to optimize the algorithm before further testing with bigger training size.

Train set  | test set| K-value | Accuracy |
-----------|---------|---------|----------|
1000      | 25     |  1      |    84 %  |
1000      | 25     |  2      |    84 %  |
1000      | 25     |  3      |    84 %  |
1000      | 25     |  4      |    84 %  |
1000      | 25     |  5      |    84 %  |
1000      | 25     |  6      |    80 %  |
1000      | 25     |  7      |    76 %  |
1000      | 25     |  8      |    68 %  |
1000      | 25     |  9      |    64 %  |
1000      | 25     |  10      |    64 %  |

More than 5 k value seems to lower accuracy significantly.





More accuracy testing to come...