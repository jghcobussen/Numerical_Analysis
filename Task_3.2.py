# -*- coding: utf-8 -*-
"""
Created on Mon May  2 19:20:18 2022

@author: joyce
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from sympy.plotting import plot

#n = 15
#arr = np.arange(-1, 1, 1/n)

#arr = [-1, -0.5, 0, 0.5, 1]
#arr = [-0.9, -0.8, 0, 0.8, 0.9]
#arr = [-1, -0.1, 0, 0.1, 1]
arr = [-1, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
print(arr)

x = Symbol('x')

#w = (x-arr[0])*(x-arr[1])*(x-arr[2])*(x-arr[3])*(x-arr[4])
w = (x-arr[1])*(x-arr[2])*(x-arr[3])*(x-arr[4])*(x-arr[5])*(x-arr[6])*(x-arr[7])*(x-arr[8])*(x-arr[9])*(x-arr[10])*(x-arr[11])*(x-arr[12])*(x-arr[13])*(x-arr[14])*(x-arr[15])*(x-arr[16])*(x-arr[17])*(x-arr[18])*(x-arr[19])
I = integrate(w, (x, 0, 1))
I_tot = 2*abs(I)
I_tot = round(I_tot, 3)
print(I_tot)

label = "Datapoints:" + str(arr) + " \n absolute integral: " + str(I_tot)
plt.rcParams['figure.figsize'] = 10, 7
plot(w, ylim=[-0.3,0.3], xlim=[-1.5,1.5], xlabel=label)