import sys

from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
import videocapture

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

    def updateStartStop(self):

        if (self.startstop.text() == "Start"):
            self.startstop.setText("Studying...")
            videocapture.backend()
        else:
            self.startstop.setText("Start")
    
    def updateDrinkWater(self):
        if (self.drinkwater.text() == "stress"):
            self.drinkwater.setText("time to work!")
        else: 
            self.drinkwater.setText("Go back to work")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())