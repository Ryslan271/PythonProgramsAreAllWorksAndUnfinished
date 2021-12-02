from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QMainWindow, QLabel
from PyQt5 import uic
import sys
from math import factorial, sqrt


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('calc.ui', self)
        self.plus.clicked.connect(self.pl)
        self.minus.clicked.connect(self.mi)
        self.sep.clicked.connect(self.se)
        self.multiple.clicked.connect(self.mult)
        self.calculate.clicked.connect(self.calcul)
        self.cl.clicked.connect(self.cli)
        self.step.clicked.connect(self.degree)
        self.fact.clicked.connect(self.fac)
        self.root.clicked.connect(self.rt)

    def cli(self):
        self.one = 0
        self.t = 0
        self.label.setText('')
        self.lineEdit.setText('')

    def pl(self):
        self.one = float(self.lineEdit.text())
        self.label.setText(self.lineEdit.text() + ' +')
        self.op = '+'
        self.lineEdit.setText('')

    def mi(self):
        self.one = float(self.lineEdit.text())
        self.label.setText(self.lineEdit.text() + ' -')
        self.op = '-'
        self.lineEdit.setText('')

    def se(self):
        self.one = float(self.lineEdit.text())
        self.label.setText(self.lineEdit.text() + ' /')
        self.op = '/'
        self.lineEdit.setText('')

    def mult(self):
        self.one = float(self.lineEdit.text())
        self.label.setText(self.lineEdit.text() + ' *')
        self.op = '*'
        self.lineEdit.setText('')

    def degree(self):
        self.one = float(self.lineEdit.text())
        self.label.setText(self.lineEdit.text() + ' ^')
        self.op = '^'
        self.lineEdit.setText('')

    def fac(self):
        self.one = int(self.lineEdit.text())
        self.label.setText(self.lineEdit.text() + '!')
        self.lineEdit.setText(str(factorial(self.one)) if self.one >= 0 else 'Error')
        self.label.setText('')

    def rt(self):
        self.one = float(self.lineEdit.text())
        self.lineEdit.setText(str(sqrt(self.one)) if self.one >= 0 else 'Error')
        self.label.setText('')

    def calcul(self):
        self.t = float(self.lineEdit.text())
        if self.one:
            if self.op == '+':
                self.lineEdit.setText(str(round(self.one + self.t)
                                          if self.one + self.t == round(self.one + self.t) else self.one + self.t))
                self.label.setText('')
            elif self.op == '-':
                self.lineEdit.setText(str(round(self.one - self.t)
                                          if self.one - self.t == round(self.one - self.t) else self.one - self.t))
                self.label.setText('')
            elif self.op == '/':
                if self.t != 0:
                    self.lineEdit.setText(str(self.one / self.t))
                    self.label.setText('')
                else:
                    self.lineEdit.setText('Error')
                    self.label.setText('')
            elif self.op == '*':
                self.lineEdit.setText(str(round(self.one * self.t)
                                          if self.one * self.t == round(self.one * self.t) else self.one * self.t))
                self.label.setText('')
            elif self.op == '^':
                self.lineEdit.setText(str(round(self.one ** int(self.t))
                                          if self.one ** int(self.t) == round(self.one ** int(self.t))
                                          else self.one ** int(self.t)))
                self.label.setText('')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec())
