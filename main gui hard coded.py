import sys
#--------------------------------------

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#--------------------------------------
import plotter
import re
#--------------------------------------
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
#--------------------------------------
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1124, 603)
        self.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(480, 10, 251, 61))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(800, 400, 200, 31))
        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(680, 400, 81, 21))
        self.label_3 = QLabel(self)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(680, 450, 71, 20))
        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(800, 450, 31, 21))
        self.lineEdit_3 = QLineEdit(self)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(960, 450, 31, 21))
        self.B1 = QPushButton(self)
        self.B1.setObjectName(u"B1")
        self.B1.setGeometry(QRect(850, 530, 93, 28))
        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(100, 90, 491, 451))
        self.PlotLay = QVBoxLayout(self.verticalLayoutWidget)
        self.PlotLay.setObjectName(u"PlotLay")
        self.PlotLay.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(850, 320, 61, 21))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_4.setFont(font1)
        self.lineEdit_4 = QLineEdit(self)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(800, 490, 31, 21))
        self.label_5 = QLabel(self)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(680, 490, 71, 20))
        self.lineEdit_5 = QLineEdit(self)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(960, 490, 31, 21))

        self.retranslateUi()
        self.setWindowIcon(QIcon('logo.png'))
        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Global", u"Plotter", None))
        self.label.setText(QCoreApplication.translate("Global",u"Function Plotter", None))
        self.label_2.setText(QCoreApplication.translate("Global",u"Function of x", None))
        self.label_3.setText(QCoreApplication.translate("Global",u"Range of x", None))
        self.B1.setText(QCoreApplication.translate("Global",u"Plot", None))
        self.label_4.setText(QCoreApplication.translate("Global", u"Inputs", None))
        self.lineEdit_4.setText("")
        self.label_5.setText(QCoreApplication.translate("Global",u"Range of y", None))
        self.lineEdit_5.setText("")
#--------------------------------------

def validate(formula_input,rangex):
    if re.search("y|u|t",formula_input) and not re.search("tan",formula_input): #checking if there are another variable other than x 
        message_box.setText(str('Please make sure that the function is in x not in y or t for example.'))
        message_box.show()#showing the message_box message
        return False
    if formula_input.count("(") != formula_input.count(")"): # for missing parenthesis
        message_box.setText(str('There is a missing parenthesis.'))
        message_box.show()
        return False
    if formula_input=="": # for no input
        message_box.setText(str('Please Enter a function of x to be plotted.'))
        message_box.show()
        return False
    try:
        rangex = [float(rangex[0]),float(rangex[1])] # for wrong range values
    except:
        message_box.setText(str('Please check range values and make sure that they are numbers.'))
        message_box.show()
        return False
    return True

def plot():
    formula_input = w.lineEdit.text() # getting input
    rangex = [w.lineEdit_2.text(),w.lineEdit_3.text()] # getting x range
    rangey = [w.lineEdit_4.text(),w.lineEdit_5.text()] # getting y range auto,auto is default
    if validate(formula_input,rangex): # validating the ranges
        rangex = [float(rangex[0]),float(rangex[1])] # converting str to float
        if [w.lineEdit_4.text(),w.lineEdit_5.text()] != ["auto","auto"]: # if default values changes then new range had been wrote down 
            rangey = [float(rangey[0]),float(rangey[1])] #str to float
        lay= w.PlotLay # getting the vBoxlayer
        yl=True # Initializing yl to be True. If default changes then it's false
        if [w.lineEdit_4.text(),w.lineEdit_5.text()] == ["auto","auto"]:
            yl = False
        fig = plotter.plot_funct(rangex,formula_input,rangey,yl) # plotting the fig and return it and save it into variable to be used
        canvas = FigureCanvas(fig) # making canvas from the figure
        lay.addWidget(canvas)# adding the figure canvas into the layer to embed the figure into the gui
        if lay.count() == 2: # Continuous ploting the adding figures into the layer so it needs to be cleaned of a number of figure more than ; equals 2
            lay.itemAt(0).widget().setParent(None) # removing the previous figure

if __name__ == "__main__": 
    app = QApplication(sys.argv)
    w=Window()
    w.setWindowIcon(QIcon('logo.png'))# putting a logo icon to the main window
    message_box = QMessageBox()#initializing message box
    message_box.setWindowTitle("Error") # title
    message_box.setWindowIcon(QIcon('logo.png'))#logo
    message_box.setText(str('Ok'))#default text for testing
    w.lineEdit_4.setText("auto")#default values for y range
    w.lineEdit_5.setText("auto")
    w.B1.clicked.connect(plot)#if plot button is clicked then call plot function
    w.show()#show app
    sys.exit(app.exec_()) # prevent the window from disapearing until the user exit i

