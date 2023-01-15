import sys
#hi sydney

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
#from layout_colorwidget import Color

# Subclass QMainWindow to customize your application's main window
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600,400)
        self.setWindowTitle("StudyCam")

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.startstop = QPushButton("Start")
        self.startstop.clicked.connect(self.updateStartStop)
        layout.addWidget(self.startstop)

        drinkwater = QPushButton("Drink water = true")

        pause = QPushButton("Pause")
        layout.addWidget(drinkwater)
        layout.addWidget(pause)

        # startstop.move(50,50)
        # drinkwater.move(250,50)
        # pause.move(50,250)

    def updateStartStop(self):
        if (self.startstop.text() == "Start"):
            self.startstop.setText("Stop")
        else:
            self.startstop.setText("Start")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())