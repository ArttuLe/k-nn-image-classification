import sys
import threading

from PyQt5.QtWidgets import QApplication

from gui.main_window import MainWindow

def main():
    """
    Main function to start application
    """
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    mainwindow.process_data()
    app.exec_()

if __name__ == "__main__":
    main()
