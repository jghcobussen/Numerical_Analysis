# -*- coding: utf-8 -*-
"""
Created on Sun May  1 18:28:49 2022

@author: joyce
"""

import numpy as np
import matplotlib.pyplot as plt

dates = [27, 28, 29, 30, 31]
days = [1,2,3,4,5]
temp = [-1.9, -3.7, -5.77, 2.53, 4.32]
energy = [109.26, 92.4, 115.33, 107.77, 61.14]

# calculate coefficients of the polynomial 
coeff = np.polyfit(days, temp, 4) #4
print(coeff)

coeff_E = np.polyfit(days, energy, 4)
print(coeff_E)

# plot the polynomial for temperature
fig = plt.figure(figsize = (10,8))
poly = np.poly1d(coeff)
new_x = np.linspace(days[0]-1, 12) #days[-1])
new_y = poly(new_x)
plt.plot(days, temp, "o", new_x, new_y, c='#1f77b4', mfc = 'r', mec = 'r')
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.xlim(0,6)
plt.ylim(-100,100)
plt.title("Polyfit polynomial")
#plt.xlim(17, 45)
plt.show()

# plot the polynomial for energy:
fig = plt.figure(figsize = (10,8))
poly = np.poly1d(coeff_E)
new_x_E = np.linspace(days[0]-1, 12) #days[-1])
new_y_E = poly(new_x)
plt.plot(days, energy, "o", new_x_E, new_y_E, c='#1f77b4', mfc = 'r', mec = 'r')
plt.xlabel('Days')
plt.ylabel('Energy')
plt.ylim(0,200)
plt.xlim(0,6)
plt.title("Polyfit polynomial")
#plt.xlim(17, 45)
plt.show()

# calculate the value of the polynomial at February 8
expect_temp = np.polyval(coeff, 8)
print("Expected temperature on February 8th with Polyfit: "+ str(expect_temp))

expect_E = np.polyval(coeff_E, 8)
print("Expected Energy usage on February 8th with Polyfit: "+ str(expect_E))


### Vandermonde approach

n = 5
m = np.vander(days, n)
print(m)

a = np.linalg.solve(m, temp)
print(a)

b = np.linalg.solve(m, energy)
print(b)

# plot the polynomial for temperatue
fig = plt.figure(figsize = (10,8))
poly = np.poly1d(a)
new_x_a = np.linspace(days[0]-1, 12) #days[-1])
new_y_a = poly(new_x_a)
plt.plot(days, temp, "o", new_x_a, new_y_a, c='#1f77b4', mfc = 'r', mec = 'r')
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.xlim(0,6)
plt.ylim(-100, 100)
plt.title("Vandermonde Polynomial")
#plt.xlim(17, 45)
plt.show()

# plot the polynomial for energy
fig = plt.figure(figsize = (10,8))
poly = np.poly1d(b)
new_x_b = np.linspace(days[0]-1, 12) #days[-1])
new_y_b = poly(new_x_b)
plt.plot(days, energy, "o", new_x_b, new_y_b, c='#1f77b4', mfc = 'r', mec = 'r')
plt.xlabel('Days')
plt.ylabel('Energy')
plt.title("Vandermonde Polynomial")
plt.ylim(0, 200)
plt.xlim(0, 6)
#plt.xlim(17, 45)
plt.show()

expect_temp = np.polyval(a, )
print("Expected temperature on February 8th with Vandermonde: "+ str(expect_temp))

expect_E = np.polyval(b, 8)
print("Expected temperature on February 8th with Vandermonde: "+ str(expect_E))


### Lagrange Interpolation

from scipy.interpolate import lagrange

x_new = np.arange(-1.0, 9, 0.1)
f = lagrange(days, temp)

### infinity norm

fig = plt.figure(figsize = (10,8))
plt.plot(x_new, f(x_new), days, temp, 'ro')
plt.title('Lagrange Polynomial')
#plt.grid()
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.xlim(0,6)
plt.ylim(-100, 100)
plt.show()

x_new = np.arange(-1.0, 9, 0.1)
f = lagrange(days, energy)

fig = plt.figure(figsize = (10,8))
plt.plot(x_new, f(x_new), days, energy, 'ro')  # w),'b', end: 'ro'
plt.title('Lagrange Polynomial')
#plt.grid()
plt.xlim(0,6)
plt.ylim(0,200)
plt.xlabel('Days')
plt.ylabel('Energy')
plt.show()