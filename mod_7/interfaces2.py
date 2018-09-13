import sys
from PyQt5.QtWidgets import (QWidget, QApplication,
                    QHBoxLayout, QVBoxLayout, QPushButton)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        okbtn = QPushButton("OK")
        cancelbtn = QPushButton("Cancel")

        horizontal = QHBoxLayout()
        horizontal.addStretch()
        horizontal.addWidget(okbtn)
        horizontal.addWidget(cancelbtn)

        vertical = QVBoxLayout()
        vertical.addStretch(1)
        vertical.addLayout(horizontal)

        self.setLayout(vertical)
        self.setWindowTitle("Horizontal Layout")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
