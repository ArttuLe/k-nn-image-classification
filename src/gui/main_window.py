from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QEvent, QModelIndex, QObject, QUrl, QThread, QObject
from PyQt5.QtWidgets import QLineEdit, QListWidgetItem, QMainWindow, QMenu, QWidget, QPushButton, QSpinBox, QLabel
from PyQt5.QtGui import QPixmap, QImage
import numpy as np

from knn import KNN
from data import Data
from prediction import Prediction


from gui.components.mainwindow import Ui_ImageClassifier

class MainWindow(QMainWindow, Ui_ImageClassifier):
    """
    Main window class
    """
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.predict = Prediction(Data(),KNN())

        # Define widgets

        self.pred_button = self.findChild(QPushButton, "predict_button")
        self.k_value = self.findChild(QPushButton, "push_test")
        self.train_size = self.findChild(QLineEdit, "training_set_size")
        self.image = self.findChild(QLineEdit, "line_image")
        self.k_value = self.findChild(QSpinBox, "k_value")
        self.image_label = self.findChild(QLabel, "label")
        self.return_label = self.findChild(QLabel, "return_label")
        self.open_button = self.findChild(QPushButton, "open_button")
        self.state = self.findChild(QLabel, "state_label")

        self.open_button.clicked.connect(self.open_image)
        self.pred_button.clicked.connect(self.predict_image)

    def open_image(self):
        num = int(self.image.text())
        image = self.predict.data.test_images[num]
        image = image.reshape(28,28)
        image = image.astype(np.uint8)
        image = QImage(image, image.shape[0],image.shape[1],QtGui.QImage.Format_RGB888)
        
        pix_map = QPixmap(image)
        pix_map = pix_map.scaled(280,280, QtCore.Qt.KeepAspectRatio)
        self.image_label.setPixmap(pix_map)

    def predict_image(self):
        """
        Predicts image loaded on the gui
        """
        
        train_size = int(self.train_size.text())
        image = int(self.image.text())
        k = int(self.k_value.text())

        ret = self.predict.predict(train_size, image, k)

        self.return_label.setText(str(ret))


        

    def run_accuracy_test(self):
        """
        Runs accuracy test on N testing images against M training images
        """