## User guide


### Instructions for running the application

The application can be started with the command mentioned in the readme file.
```sh
poetry run invoke start
```
The start of the application is slow, as all the data is being loaded and processed into memory while the program starts.

- Start running the program by opening an image with the file explorer.
- Input the desired training set and k -values
- Press the "predict" button

As of now there is no indication about the state of the application, and the main GUI thread will freeze when the prediction is being run.
The prediction is done when the predicted number pops up on the output field.


### Instructions for running the accuracy testing

Accuracy testing is used to test the overall accuracy of the algorithm with multiple test images.

Command for starting the accuracy testing.

```sh
poetry run invoke test
```

After starting the testing program, all you do is input the desired training set size and testing set size and the k-value.
The application then starts running the test. 
As of now, there is no indication of any progress of the tests being run.



