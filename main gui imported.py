import sys
import warnings
warnings.filterwarnings("ignore")
#--------------------------------------
from PySide2.QtWidgets import QApplication,QMessageBox
from PySide2 import QtUiTools,QtGui
#--------------------------------------
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#--------------------------------------
import plotter
import re
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
    w = QtUiTools.QUiLoader().load("plotter.ui") # loading the design from qt designer file
    w.setWindowIcon(QtGui.QIcon('logo.png'))# putting a logo icon to the main window
    message_box = QMessageBox()#initializing message box
    message_box.setWindowTitle("Error") # title
    message_box.setWindowIcon(QtGui.QIcon('logo.png'))#logo
    message_box.setText(str('Ok'))#default text for testing
    w.lineEdit_4.setText("auto")#default values for y range
    w.lineEdit_5.setText("auto")
    w.B1.clicked.connect(plot)#if plot button is clicked then call plot function
    w.show()#show app
    sys.exit(app.exec_()) # prevent the window from disapearing until the user exit it