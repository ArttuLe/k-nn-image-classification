
## Unit Testing




### Distance metrics

Distance calculations are the only tests that are run using the automated tools. Accuracy testing etc. are run using the testing version of the application.


### Manual accuracy testing

Manual accuracy testing needs to be run in order to validate the accuracy of the algorithm



Below are accuracy tests with different sized training sets and testing sets.


Train set  | test set| K-value | Accuracy |
-----------|---------|---------|----------|
10000      | 500     |  3      |    96 %  |
1000        | 120     |  3      |    86 %  |
5000       | 120    |  3      |     92%  |
5000       | 480    |  3      |     89%  |
7500       | 720    |  3      |     90%  |
10000       | 1200    |  4      |     90%  |
 .       | .    |  .      |     %  |
 .       | .    |  .      |     %  |
 .       | .    |  .      |     %  |
 .       | .    |  .      |     %  |
 .       | .    |  .      |     %  |
 .       | .    |  .      |     %  |
 .       | .    |  .      |     %  |

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