# -*- coding: utf-8 -*-
"""
Created on Wed May  4 11:07:22 2022

@author: joyce
"""

from sympy import *
from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt
import math

def cubspline(xint, yint):
    h = xint[1]-xint[0]
    print(h)

    m = len(xint)
    matrix = np.zeros((m-1, m-1))
    y = np.zeros((m-1,1))
    
    matrix[0][0] = 4
    for i in range(1, len(y)):
        matrix[i][i] = 4
        matrix[i-1][i] = 1
        matrix[i][i-1] = 1
    for i in range(0, len(y)):
        y[i] = yint[i+1] - 2*yint[i] - yint[i-1]
        
    print(matrix)
    print(y)
    
    sigma = np.linalg.solve(matrix, y)
    print(sigma)
    
    mc = np.zeros((m-1,4))
    for i in range (0, m-2):
        mc[i][0] = yint[i]
        mc[i][2] = sigma[i]/2
        mc[i][3] = (sigma[i+1]- sigma[i])/(6*h)
        mc[i][1] = (yint[i+1] - yint[i])/h - (h/6)*(2*sigma[i] + sigma[i+1])
    
    print(mc)
    return mc

def cubsplineval(coeff,xint,xval):
    h = xint[1]-xint[0]
    spline = floor(xval/h)-1
    print(spline)
    a = coeff[spline][0]
    b = coeff[spline][1]
    c = coeff[spline][2]
    d = coeff[spline][3]
    
    xi = xint[spline]
    x = Symbol('x')
    s = a + b*(x-xi) + c*(x-xi)**2 + d*(x-xi)**3
    value = s.subs(x, xval)
    print(value)
    
    return value

x = [1, 2, 3, 4, 5]
y = [-1.9, -3.7, -5.77, 2.53, 4.32]

test = cubspline(x,y)
value = cubsplineval(test, x, 1.5)

# calculate coefficients of the polynomial 
coeff = np.polyfit(x, y, 4) #4
print(coeff)

from sympy.plotting.plot import MatplotlibBackend, Plot
def get_sympy_subplots(plot: Plot):
    backend = MatplotlibBackend(plot)

    backend.process_series()
    backend.fig.tight_layout()
    return backend.fig, backend.ax[0]

def plotter(coeff, s, xint, yint):
    a = coeff[s][0]
    b = coeff[s][1]
    c = coeff[s][2]
    d = coeff[s][3]
    
    xi = xint[s]
    x = Symbol('x')
    s = a + b*(x-xi) + c*(x-xi)**2 + d*(x-xi)**3
    p = plot(s, ylim=[-9, 5], xlim=[0, 5]) #xlabel=label)
    fig, axe = get_sympy_subplots(p)
    axe.plot(xint, yint, "o")

for i in range(0, 4):
    plotter(test, i, x, y)

fig = plt.figure(figsize = (10,8))
#poly = np.poly1d(np.flip(test[0]))
poly = np.poly1d(coeff)
new_x = np.linspace(x[0], x[-1]) #days[-1])
new_y = poly(new_x)
plt.plot(x, y, "o", new_x, new_y, c='#1f77b4', mfc = 'r', mec = 'r')
plt.xlabel('x')
plt.ylabel('y')
#plt.xlim(0,6)
#plt.ylim(-100,100)
plt.title("Polyfit polynomial")
#plt.xlim(17, 45)
plt.show()

