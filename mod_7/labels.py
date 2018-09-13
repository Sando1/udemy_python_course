import sys
from PyQt5.QtWidgets import (QWidget, QApplication,
                    QHBoxLayout, QVBoxLayout, QPushButton, QLabel,
                    QLineEdit)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.counter = 0

    def init_ui(self):

        self.text_label = QLabel("No Name. Cant do Anything")
        self.label = QLabel("Name: ")
        self.name_input = QLineEdit()
        self.btn = QPushButton("Set Name")
        self.btn.clicked.connect(self.alterName)

        h = QHBoxLayout()
        h.addWidget(self.label)
        h.addWidget(self.name_input)

        v = QVBoxLayout()
        v.addWidget(self.text_label)
        v.addLayout(h)
        v.addWidget(self.btn)

        self.setLayout(v)
        self.setWindowTitle("Nothing has been clicked")
        self.show()

    def alterName(self):
        inputted = self.name_input.text()
        our_string = "You entered {}".format(inputted)
        self.text_label.setText(our_string)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
