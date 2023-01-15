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

        self.drinkwater = QPushButton("Drink Water Alarm is off")
        self.drinkwater.clicked.connect(self.updateDrinkWater)
        layout.addWidget(self.drinkwater)

    def updateStartStop(self):

        if (self.startstop.text() == "Start"):
            videocapture.backend()
            self.startstop.setText("Stop")
        else:
            self.startstop.setText("Start")
    
    def updateDrinkWater(self):
        if (self.drinkwater.text() == "Drink Water Alarm is off"):
            self.drinkwater.setText("Drink Water Alarm is set! Click again to reset.")
        else: 
            self.drinkwater.setText("Drink Water Alarm is off")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())