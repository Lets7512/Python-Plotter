import parser
from math import *
import matplotlib.pyplot as plt
import numpy as np
#from numpy import *
#--------------------------------------
def solve_y_for_x(formula,x_in):
    formula = formula.replace("^","**")
    code = parser.expr(formula).compile()
    x=x_in
    return eval(code)

#--------------------------------------
def plot_funct(rangex,formula_input,rangey,yl):
    formula = formula_input.replace("^","**") # formating input
    formula = formula.replace("e","exp(1)") # formating input
    if formula_input.find("log") !=-1:
        formula = formula.replace("log","log10") # formating input
    formula = formula.replace("ln","log") # formating input
    code = parser.expr(formula).compile() # parsing the input into variables of x , sin(x) , exp(x) ,etc
    y=[] # storing y values for plotting
    x_plot=[] # storing x values for plotting
    start = rangex[0] # start point 
    end = rangex[1] # end point 
    rangex=np.linspace(start,end,int(abs(start-end*100))+1,endpoint=True) # numpy array for x values including the end point
    for i in rangex:
        x=i #assigning the x with values of numpy array to be evaluated by eval function
        try:
            result = eval(code) # getting y value
        except: # expecting division by zero
            continue 
        y.append(result) # appending result to y list
        x_plot.append(x) # appending result to x plot list
    y=np.array(y,dtype=float) # converting y to numpy array to filter it
    x_plot=np.array(x_plot,dtype=float) #coverting x to numpy array to match the type of y for plotting 
    y[:-1][np.diff(y) < -100] = np.nan # omitting the joint line between disconnected points on graph
    fig = plt.figure() # initializing figure
    plt.plot(x_plot,y) # ploting the values
    plt.ylabel("$\mathrm{y}$",rotation=0) # xlabel
    plt.xlabel("$\mathrm{x}$")#ylabel
    plt.title('Plot of function: $\mathrm{'+formula_input+'}$')#title
    if yl == True: # this is for limiting the range of y axis. and make it possible to set it as auto and as custom from user
        plt.ylim([rangey[0],rangey[1]]) # y axis range limiting 
    plt.grid() # puting grid
    #plt.show()
    return fig

#--------------------------------------
if  __name__ == "__main__":
    pass
    #rangex=[float(-10),float(10)]
    #rangey=[float(-100),float(100)]
    #formula_input = "tan(x)"
    #plot_funct(rangex,formula_input,rangey)