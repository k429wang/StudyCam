import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
#from layout_colorwidget import Color

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600,400)
        self.setWindowTitle("StudyCam")

        self.setWindowTitle("My App")
        layout = QVBoxLayout()

        startstop = QPushButton("Start", self)
        startstop.clicked.connect(self.updateStartStop)

        drinkwater = QPushButton("Drink water = true", self)

        pause = QPushButton("Pause", self)

        startstop.move(50,50)
        drinkwater.move(250,50)
        pause.move(50,250)

    def updateStartStop(self):
        print("hi")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())