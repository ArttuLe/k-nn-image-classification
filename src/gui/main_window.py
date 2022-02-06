from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QEvent, QModelIndex, QUrl, QThread, QObject, pyqtSignal
from PyQt5.QtWidgets import QLineEdit, QListWidgetItem, QMainWindow, QFileDialog, QWidget, QPushButton, QSpinBox, QLabel
from PyQt5.QtGui import QPixmap, QImage
import numpy as np
import os

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
        self.predict = Prediction(KNN())

        # Define widgets
        self.statusbar.showMessage("Ready...")
        self.pred_button = self.findChild(QPushButton, "predict_button")
        self.k_value = self.findChild(QPushButton, "push_test")
        self.train_size = self.findChild(QLineEdit, "training_set_size")
        self.k_value = self.findChild(QSpinBox, "k_value")
        self.image_label = self.findChild(QLabel, "label")
        self.return_label = self.findChild(QLabel, "return_label")
        self.open_button = self.findChild(QPushButton, "open_button")
        self.progress = self.findChild(QLabel, "progress_label")

        self.open_button.clicked.connect(self.open_image)
        self.pred_button.clicked.connect(self.predict_image)

    def open_image(self):
        fname = QFileDialog.getOpenFileName(
            self, "Open image", "/home/koulu/k-nn-image-classification/data/images/", "PNG Files (*.png)")
        
        self.im_index = os.path.basename(fname[0])
        self.im_index = self.im_index[:-4]

        self.pixmap = QPixmap(fname[0])
        self.pixmap = self.pixmap.scaled(280,280, QtCore.Qt.KeepAspectRatio)
        self.image_label.setPixmap(self.pixmap)

    def process_data(self):
        self.data = Data()

    def report_progress(self,n):
        self.progress.setText("Progress: {n}/500")


    def predict_image(self):
        """
        Predicts image loaded on the gui
        """
        train_size = int(self.train_size.text())
        image = int(self.im_index)
        k = int(self.k_value.text())

        ret = self.predict.predict(
        self.data.train[:train_size], self.data.train_labels[:train_size], self.data.test[image], k
        )

        self.return_label.setText(str(ret))
        self.statusbar.showMessage("Ready...")


        

    def run_accuracy_test(self):
        """
        Runs accuracy test on N testing images against M training images
        """
        for i in range(500):
            


            self.report_progress(i+1)

class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self):
        
        self.finished.emit()