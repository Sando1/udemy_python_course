import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import math

class Button(object):
    """docstring for Button
    this class will initialise the button widget
    each button will have its own handlers which will
    handle and evaluate results """
    def __init__(self, text, results):
        self.b = QPushButton(str(text))
        self.text = text
        self.results = results
        self.b.clicked.connect(lambda: self.handleInput(self.text))

    def handleInput(self, v):
        if v == "=" :
            res = eval(self.results.text())
            self.results.setText(str(res))
        elif v == "<":
            curr = self.results.text()
            self.results.setText(curr[:-1])
        elif v == "AC":
            self.results.setText("")
        elif v == "sqrt":
            val = float(self.results.text())
            self.results.setText(str(math.sqrt(val)))
        else:
            curr = self.results.text()
            new = curr + str(v)
            self.results.setText(new)



class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.CreateApp()


    def CreateApp(self):
        #Grid Layout used
        grid = QGridLayout()
        #an input and results line which is in the first row and first column
        #and it is one row high and spans 4 columns
        result = QLineEdit()
        grid.addWidget(result, 0, 0, 1, 4)

        #a list of buttons with actual integers so that
        #performing calculations is easy.
        buttons = ["AC","sqrt", "%","/",
                7,8,9,"*",
                4,5,6,"-",
                1,2,3,"+",
                0,".","=","<"]

        #since the first row is take by the results var
        #the buttons will start from the second row
        row = 1
        col = 0
        # a loop to initilise the buttons
        # where the col variable it reset at 3 to ensure that only
        # cols in each row.
        # each button is first initialised in the button class.
        # each button takes 1 col and 1 row
        # makes it a grid layout.
        for button in buttons:
            if col > 3:
                col = 0
                row +=1
            buttonObject = Button(button, result)
            grid.addWidget(buttonObject.b, row, col, 1, 1)
            col +=1

        self.setLayout(grid)
        self.show()

#starting and running application commands
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec_())
