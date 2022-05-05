# -*- coding: utf-8 -*-
"""
Created on Tue May  3 20:12:23 2022

@author: joyce
"""


import numpy as np
import matplotlib.pyplot as plt
Abs
from sympy import *
from sympy.plotting import plot

x = Symbol('x')

arr_3 = [-1, 0, 1]
#arr_3 = [-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1]
#arr_3 = [-1, -6/7, -5/7, -4/7, -3/7, -2/7, -1/7, 0, 1/7, 2/7, 3/7, 4/7, 5/7, 6/7, 1]

f = 1/(1+25*x**2)
true_f = []
plot_f = []
for i in range(0, len(arr_3)):
    true_f.append(float(f.subs(x, arr_3[i])))
print(true_f)

points = np.linspace(-1, 1, 500)
for i in range (0, len(points)):
    plot_f.append(float(f.subs(x, points[i])))

# calculate coefficients of the polynomial 
coeff = np.polyfit(arr_3, true_f, 14) #4
print(coeff)

# plot the polynomial
fig = plt.figure(figsize = (10,8))
poly = np.poly1d(coeff)
new_x = np.linspace(arr_3[0], arr_3[-1]) #days[-1])
new_y = poly(new_x)
plt.plot(arr_3, true_f, "o", new_x, new_y, c='#1f77b4', mfc = 'r', mec = 'r')
plt.plot(points, plot_f, c='black', linewidth = 0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.ylim(0, 1)
#plt.xlim(0,6)
#plt.ylim(-100,100)
plt.title("Polyfit polynomial with n=3")
#plt.xlim(17, 45)
plt.show()

#____________________________________________________________________
# Chebyshev
#____________________________________________________________________

arr = np.polynomial.chebyshev.chebpts1(15)

f = 1/(1+25*x**2)
true_f = []
plot_f = []
for i in range(0, len(arr)):
    true_f.append(float(f.subs(x, arr[i])))
print(true_f)

points = np.linspace(-1, 1, 500)
for i in range (0, len(points)):
    plot_f.append(float(f.subs(x, points[i])))

# calculate coefficients of the polynomial 
coeff = np.polyfit(arr, true_f, 14) #4
print(coeff)

x = Symbol('x')

fig = plt.figure(figsize = (10,8))
poly = np.poly1d(coeff)
new_x = np.linspace(arr[0], arr[-1]) #days[-1])
new_y = poly(new_x)
plt.plot(arr, true_f, "o", new_x, new_y, c='#1f77b4', mfc = 'r', mec = 'r')
plt.plot(points, plot_f, c='black', linewidth = 0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.ylim(0, 1)
#plt.xlim(0,6)
#plt.ylim(-100,100)
plt.title("Polyfit polynomial with n=15 chebyshev points")
plt.show()

'''
label = "Datapoints:" + str(np.round(arr, 4)) + " \n absolute integral: " + str(I_tot)
plt.rcParams['figure.figsize'] = 10, 7
plot(f, ylim=[-0.3,0.3], xlim=[-1.5,1.5], xlabel=label)
'''
