from time import sleep

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from sixteen15ui import *
from random import randint
import sys


class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.buttons = [[self.ui.btn1, self.ui.btn2, self.ui.btn3, self.ui.btn4],
                        [self.ui.btn5, self.ui.btn6, self.ui.btn7, self.ui.btn8],
                        [self.ui.btn9, self.ui.btn10, self.ui.btn11, self.ui.btn12],
                        [self.ui.btn13, self.ui.btn14, self.ui.btn15, self.ui.btn16]]

        self.trueAnswer = [[self.ui.btn1, self.ui.btn2, self.ui.btn3, self.ui.btn4],
                           [self.ui.btn5, self.ui.btn6, self.ui.btn7, self.ui.btn8],
                           [self.ui.btn9, self.ui.btn10, self.ui.btn11, self.ui.btn12],
                           [self.ui.btn13, self.ui.btn14, self.ui.btn15, self.ui.btn16]]
        self.makeTheCubicRand()
        self.showAll()

        self.ui.btn1.clicked.connect(lambda: self.btnClicked(self.ui.btn1))
        self.ui.btn2.clicked.connect(lambda: self.btnClicked(self.ui.btn2))
        self.ui.btn3.clicked.connect(lambda: self.btnClicked(self.ui.btn3))
        self.ui.btn4.clicked.connect(lambda: self.btnClicked(self.ui.btn4))
        self.ui.btn5.clicked.connect(lambda: self.btnClicked(self.ui.btn5))
        self.ui.btn6.clicked.connect(lambda: self.btnClicked(self.ui.btn6))
        self.ui.btn7.clicked.connect(lambda: self.btnClicked(self.ui.btn7))
        self.ui.btn8.clicked.connect(lambda: self.btnClicked(self.ui.btn8))
        self.ui.btn9.clicked.connect(lambda: self.btnClicked(self.ui.btn9))
        self.ui.btn10.clicked.connect(lambda: self.btnClicked(self.ui.btn10))
        self.ui.btn11.clicked.connect(lambda: self.btnClicked(self.ui.btn11))
        self.ui.btn12.clicked.connect(lambda: self.btnClicked(self.ui.btn12))
        self.ui.btn13.clicked.connect(lambda: self.btnClicked(self.ui.btn13))
        self.ui.btn14.clicked.connect(lambda: self.btnClicked(self.ui.btn14))
        self.ui.btn15.clicked.connect(lambda: self.btnClicked(self.ui.btn15))
        self.ui.btnsubmit.clicked.connect(self.submitPressed)

    def submitPressed(self):
        self.warningMsg()

    def warningMsg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Warning!!!")
        msg.setText("Do you really want to submit?\n"
                    "If you do so what you have done will be gone\n"
                    "and your score will be added to your credits")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        res = msg.exec()
        if res == QMessageBox.StandardButton.Yes:
            # score will be added users database

            if self.isWin():
                score = 100
            else:
                temp = 0
                for i in range(4):
                    for j in range(4):
                        if self.trueAnswer[i][j] == self.buttons[i][j]:
                            temp +=1
                score = temp
            while True:
                sleep(3)
                break
            self.makeTheCubicRand()
            self.showAll()


    def isWin(self):
        for i in range(4):
            for j in range(4):
                if self.trueAnswer[i][j] != self.buttons[i][j]:
                    return False
        return True

    def makeTheCubicRand(self):
        for i in range(4):
            for j in range(4):
                for k in range(randint(2, 3)):
                    for l in range(randint(1, 3)):
                        t = self.get_indexes(self.buttons[i][j])
                        y1, x1 = t[0], t[1]
                        t1 = self.get_indexes(self.buttons[k][l])
                        y2, x2 = t1[0], t1[1]
                        self.swapTwoGeometry(self.buttons[y1][x1], self.buttons[y2][x2])
                        self.swapOrderInButtons(y1, x1, y2, x2)

    def get_indexes(self, button):
        for j in range(4):
            for i in range(4):
                if self.buttons[j][i] == button:
                    return [j, i]

    def swapTwoGeometry(self, button1, button2):
        temp = button1.geometry()
        button1.setGeometry(button2.geometry())
        button2.setGeometry(temp)

    def swapOrderInButtons(self, y1, x1, y2, x2):
        self.buttons[y1][x1], self.buttons[y2][x2] = self.buttons[y2][x2], self.buttons[y1][x1]

    def showAll(self):
        for i in range(4):
            for j in range(4):
                if self.trueAnswer[i][j] == self.buttons[i][j]:
                    self.buttons[i][j].setStyleSheet("background-color: rgb(51, 209, 122);")
                else:
                    self.buttons[i][j].setStyleSheet("background-color: rgb(255, 190, 111);")
                self.buttons[i][j].show()

    def btnClicked(self, button):
        index_x = index_y = 0
        index16_x = index16_y = 0

        for i in range(4):
            for j in range(4):
                if self.buttons[i][j] == button:
                    index_y = i
                    index_x = j
                if self.buttons[i][j] == self.ui.btn16:
                    index16_y = i
                    index16_x = j

        available = [0, 1, 2, 3]
        if index_y + 1 in available and index16_x == index_x and index16_y == index_y + 1:
            self.swapTwoGeometry(button, self.ui.btn16)
            self.swapOrderInButtons(index_y, index_x, index16_y, index16_x)
        elif index_y - 1 in available and index16_x == index_x and index16_y == index_y - 1:
            self.swapTwoGeometry(button, self.ui.btn16)
            self.swapOrderInButtons(index_y, index_x, index16_y, index16_x)
        elif index_y == index16_y and abs(index_x - index16_x) == 1:
            self.swapTwoGeometry(button, self.ui.btn16)
            self.swapOrderInButtons(index_y, index_x, index16_y, index16_x)
        self.showAll()


def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
