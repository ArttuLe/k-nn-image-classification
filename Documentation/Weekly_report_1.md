# Week 1

- [Hours](https://github.com/ArttuLe/k-nn-image-classification/blob/main/Documentation/Hours.md)

## Weekly report no. 1

### Things that i've done this week
- Read lots about k-nn and the different kind of metrics used to calculate the distances
- Tried to understand the main idea of the k-nn algorithm
- Setup github, although everything is failing at the moment...
- Some coding...


### Progression
- Successfully made a working minimum version of the application, and it seems to be working as intended, if i understood the idea of the algorithm correctly.
- Testing is set up and running. Only 1 test running for loading the data correctly so far.
- Pylint is set up for code style checking
- Decent progression on understanding the topic.

### What i've learned so far
- The basic concept of the k-nearest neighbours algorithm
- How the k-nn uses different kinds of metrics to calculate the distances
- How to read and maybe understand scientific publications on topics


### Next up...
- More reading on the topic
- Look into k-fold cross validation
- Implement the hausdorff modified distance for better results?


### Questions
- Am i to implement the heap myself for keeping up with the k nearest neighbours? is the heap even necessary for the task?
- Are numpy etc. acceptable to use?
- Is my implementation of the euclidean distance correct? are the hausdorff modified distances basically euclidean distance+some extra? Having some trouble understanding the d6-distance notation in the paper linked on the course site.
- do i need to plot the k-nn stuff for the visualization or is it enough to display the image to be predicted and then the prediction in text somewhere in the gui?