# Week 2

- [Hours](https://github.com/ArttuLe/k-nn-image-classification/blob/main/Documentation/Hours.md)

## Weekly report no. 2

### Things that i've done this week
- Coding
- read some papers about calculating distances between two point sets


### Progression
- Ran a successful test with 10000 training set and 25 test images and got 96% accuracy.
- Started working on the GUI for the application

### What i've learned so far
- The math behind calculating nearest neighbours using distance between point sets
- More GUI programming with pyQT


### Next up...
- Tests! and figure out what parts to test.
- More development on the GUI
- Validate that the algorithm is really working as intended.
- Maybe try a bit more complex distance metric
- Need to get all the data processing parts out of the prediction part, need to run all processing of the data before predicting
- Clean up the code, getting a bit messy...


### Questions
- Does the calculations for the distances look ok?
- Testing takes time... Could parallelization speed things up? for example split image into 4 or 8 rows of pixels and pass them to separate threads, or multiple images being processed simultaneously?
- How does the algorithm look?