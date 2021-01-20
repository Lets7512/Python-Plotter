import pytest
import plotter

def test_formulas():
    assert plotter.solve_y_for_x("x^2+1",2) == 5
    assert round(plotter.solve_y_for_x("pi",3.14),2) == round(3.14,2)
    assert round(float(plotter.solve_y_for_x("sin(pi)+x",1)),5) == round(float(1),5)
    assert round(float(plotter.solve_y_for_x("sin(x)^2+cos(x)^2",1)),5) == round(float(1),5)
    assert round(float(plotter.solve_y_for_x("exp(x)",3)),3) == float(20.086)
    assert round(float(plotter.solve_y_for_x("e^x",3)),3) == float(20.086)
    #assert plotter.solve_y_for_x("y^2+1",2) == 5