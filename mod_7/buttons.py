import sys
from PyQt5.QtWidgets import (QWidget, QApplication,
                    QHBoxLayout, QVBoxLayout, QPushButton)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.counter = 0

    def init_ui(self):
        self.btn = QPushButton("Clicked: 0")
        self.btn.clicked.connect(self.clickedButton)

        v = QVBoxLayout()
        v.addWidget(self.btn)

        self.setLayout(v)
        self.setWindowTitle("Clicking Buttons")
        self.show()

    def clickedButton(self):
        self.counter += 1
        self.btn.setText('Counter: {}'.format(self.counter))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
