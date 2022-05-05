# -*- coding: utf-8 -*-
"""
Created on Tue May  3 14:09:43 2022

@author: joyce
"""

'''
import numpy as np

cheb = np.polynomial.chebyshev.Chebyshev((0,0,0,0,0,1))
coef = np.polynomial.chebyshev.cheb2poly(cheb.coef)
'''

from mpmath import chebyt, chop, taylor
import numpy as np
from sympy import *
from sympy.plotting import plot
import matplotlib.pyplot as plt

arr = np.polynomial.chebyshev.chebpts1(9)

x = Symbol('x')
#w = (x-arr[0])*(x-arr[1])*(x-arr[2])*(x-arr[3])*(x-arr[4])
w = (x-arr[0])*(x-arr[1])*(x-arr[2])*(x-arr[3])*(x-arr[4])*(x-arr[5])*(x-arr[6])*(x-arr[7])*(x-arr[8])#*(x-arr[9])*(x-arr[10])*(x-arr[11])*(x-arr[12])*(x-arr[13])*(x-arr[14])*(x-arr[15])*(x-arr[16])*(x-arr[17])*(x-arr[18])*(x-arr[19])
I = integrate(w, (x, 0, 1))
I_tot = 2*abs(I)
I_tot = round(I_tot, 3)
print(I_tot)

label = "Datapoints:" + str(np.round(arr, 4)) + " \n absolute integral: " + str(I_tot)
plt.rcParams['figure.figsize'] = 10, 7
plot(w, ylim=[-0.3,0.3], xlim=[-1.5,1.5], xlabel=label)

 